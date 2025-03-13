from django.shortcuts import redirect, render, get_object_or_404
from .models import Article, ArticleImage, Category
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
    ordering = ['-created_at']

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

        new_category_name = form.cleaned_data.get('new_category')
        new_category_description = form.cleaned_data.get('new_category_description')
        if new_category_name:
            category, created = Category.objects.get_or_create(
                name=new_category_name,
                description=new_category_description
            )

        if new_category_name:
            article.category.add(category)

        images = self.request.FILES.getlist('files')
        for image in images:
            ArticleImage.objects.create(
                article=article,
                image=image,
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
def delete_note_image(request, note_pk, pk):
    article = get_object_or_404(Article, pk=note_pk, owner=request.user)
    image = get_object_or_404(ArticleImage, pk=pk, article=article)
    image.delete()
    # messages.success(request, 'Файл удален')
    return redirect('article_update', pk=article.pk)


class UpdateArticleView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    template_name = 'news/update_article.html'
    form_class = ArticleForm

    def form_valid(self, form):

        # Обрабатываем новые теги
        new_category_name = form.cleaned_data.get('new_category')
        if new_category_name:
            category, created_at = Category.objects.get_or_create(
                name=new_category_name,
            )
            self.object.category.add(category)

        # Обрабатываем новые файлы
        files = self.request.FILES.getlist('files')
        for file in files:
            ArticleImage.objects.create(
                article=self.object,
                file=file,
            )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_categories'] = Category.objects.exists()
        return context


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

        if image := article.files.all():
            for image in image:
                email.attach_file(image.image.path)

        return email.send()


class ToggleFavoriteView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        if request.user in article.favorites.all():
            article.favorites.remove(request.user)
            messages.success(self.request, 'Added to favorites')
        else:
            article.favorites.add(request.user)
            messages.success(self.request, 'Removed from favorites')
        article.save()
        return redirect('index')
