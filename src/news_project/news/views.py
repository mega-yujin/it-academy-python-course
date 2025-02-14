from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category, ArticleImage,FavoriteArticle
from django.views import View, generic
from django.urls import reverse_lazy, reverse
from .forms import ArticleModelForm, ArticleImageForm, EmailArticleForm
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

# def index(request: HttpRequest):
#     context = {
#         'news' : Article.objects.all(),
#     }
#     return render(request, 'index.html', context)

class HomeView(generic.ListView):
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.prefetch_related('categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_favorites'] = set(FavoriteArticle.objects.filter(user=self.request.user).values_list('article_id', flat=True))
        else:
            context['user_favorites'] = set()  # Для анонимных пользователей
        return context

class FavoritesView(
    LoginRequiredMixin,
    generic.ListView,
):
    model = FavoriteArticle
    template_name = 'news/favorites.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    def get_queryset(self):
        return FavoriteArticle.objects.filter(user=self.request.user).select_related('article')

class ToggleFavoriteView(LoginRequiredMixin, View):

    @method_decorator(require_POST)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        favorite, created = FavoriteArticle.objects.get_or_create(user=request.user, article=article)
        if not created:
            favorite.delete()
        return redirect('index')

# def add_article(request: HttpRequest):
#     if request.method == 'POST':
#         form_data = request.POST.dict()
#         note = Article(
#             title=form_data.get('title'),
#             content=form_data.get('content'),
#             author_id=1,
#             )
#         note.save()
#         return redirect('index')
#     return render(request, 'add_article.html')

# def article_detail(request, article_id):
#     context = {
#         'article' : get_object_or_404(Article, id=article_id)
#     }
#     return render(request, 'article_detail.html', context)

class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).prefetch_related('images')

class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'news/article_confirm_delete.html'
    success_url = reverse_lazy('index')

class AddArticleView(LoginRequiredMixin, generic.CreateView):
    model = Article
    form_class = ArticleModelForm
    template_name = 'news/add_article.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        form.save_m2m()

        new_category_name = form.cleaned_data.get('new_category')
        if new_category_name:
            category, created = Category.objects.get_or_create(name=new_category_name)
            article.categories.add(category)

        images = self.request.FILES.getlist('images')
        for image in images:
            ArticleImage.objects.create(
                article=article,
                image=image,
            )

        return redirect('article_detail', pk=article.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_catigories'] = Category.objects.exists()
        return context
#
# class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Article
#     form_class = ArticleModelForm
#     template_name = 'news/add_article.html'
#
#     def get_success_url(self):
#         return reverse_lazy('article_detail', kwargs={'pk': self.object.pk})

class ShareArticleView(FormView):
    template_name = 'news/share_article.html'
    email_template = 'email/share_article.html'
    form_class = EmailArticleForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.get_article()
        return context

    def get_article(self):
        return get_object_or_404(Article, pk=self.kwargs['pk'])

    def form_valid(self, form):
        article = self.get_article()
        try:
            self.send_article_email(
                article=article,
                to_email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(
                self.request,
                f'Статья успешно отправлена на {form.cleaned_data["email"]}'
            )
        except Exception as e:
            messages.error(
                self.request,
                f'Произошла ошибка при отправке статьи:{e}. Попробуйте позже.'
            )
        return super().form_valid(form)

    def send_article_email(self, article, to_email, message=None):
        subject = f'Статья: {article.title}'
        context = {
            'article': article,
            'message': message
        }

        html_content = render_to_string('email/share_article.html', context)

        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=None,
            to=[to_email],
            reply_to=[article.author.email] if article.author.email else None,
        )
        email.content_subtype = "html"

        if image := article.images.all():
            for image in image:
                email.attach_file(image.image.path)

        return email.send()