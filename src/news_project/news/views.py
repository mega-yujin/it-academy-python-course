from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, ArticleFile
from .forms import ArticleForm, ArticleEmailForm
# from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
import logging
from django.template.loader import render_to_string

# Create your views here.


class HomeView(LoginRequiredMixin, generic.ListView):
    model = Article
    context_object_name = 'articles'

    # def get_queryset(self):
    #     return Article.objects.prefetch_related('tags').filter(owner=self.request.user)


# def article_list(request):
#     article = Article.objects.all()
#     return render(request, 'news/article_list.html', {'articles': article})


# def article_detail(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     return render(request, 'news/article_detail.html', {'article': article})


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'


# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('article_list')
#     else:
#         form = ArticleForm()
#     users = User.objects.all()
#     # User.objects.save(username='Bob', password='1234')
#     return render(request, 'news/add_article.html', {'form': form, 'users': users})


class AddArticleView(LoginRequiredMixin, generic.CreateView):
    form_class = ArticleForm
    template_name = 'news/add_article.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.owner = self.request.user
        article.save()
        form.save_m2m()

        files = self.request.FILES.getlist('files')
        for file in files:
            ArticleFile.objects.create(
                article=article,
                file=file,
            )

        return redirect('article_detail', pk=article.pk)


# def delete_article(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         article.delete()
#         return redirect('article_list')
#     return render(request, 'news/delete_article.html', {'article': article})


class DeleteArticleView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    template_name = 'news/delete_article.html'
    success_url = reverse_lazy('index')
    context_object_name = 'article'


@login_required
def delete_note_file(request, note_pk, pk):
    article = get_object_or_404(Article, pk=note_pk, owner=request.user)
    file = get_object_or_404(ArticleFile, pk=pk, article=article)
    file.delete()
    # messages.success(request, 'Файл удален')
    return redirect('article_update', pk=article.pk)


class UpdateArticleView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    template_name = 'news/update_article.html'
    success_url = reverse_lazy('index')
    fields = ['title', 'content']


class ShareArticleView(generic.FormView):
    template_name = 'news/share_article.html'
    email_template = 'email/article_email_share_body.html'
    form_class = ArticleEmailForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['article'] = self.get_article()
        return context

    def get_article(self):
        return get_object_or_404(Article, pk=self.kwargs['pk'])

    def form_valid(self, form):
        try:
            self.send_mail(
                self.get_article(),
                form.cleaned_data['email'],
                form.cleaned_data['message'],
            )
            logging.info(f'Email sent to {form.cleaned_data["email"]}')
            messages.success(self.request, 'Email sent')
        except Exception as err:
            logging.warning(f'Error: {err}. Try again later.')
            messages.error(self.request, 'Error')

        return super().form_valid(form)

    def send_mail(self, article: Article, to_email: str, message: str = None):
        # raise Exception('SOME CRITICAL EXCEPTION!!!')
        html_content = render_to_string(
            self.email_template,
            {
                'article': article,
                'message': message,
            }
        )

        email = EmailMultiAlternatives(
            subject=f'Article {article.title}',
            body=html_content,
            from_email=None,
            to=[to_email],
            reply_to=[article.owner.email] if article.owner.email else None
        )
        email.content_subtype = 'html'

        if file := article.files.all():
            for file in file:
                email.attach_file(file.file.path)

        return email.send()
