from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category, ArticleImage
from django.views import View, generic
from django.urls import reverse_lazy
from .forms import ArticleModelForm, ArticleImageForm, EmailArticleForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.core.mail import send_mail

# def index(request: HttpRequest):
#     context = {
#         'news' : Article.objects.all(),
#     }
#     return render(request, 'index.html', context)

class HomeView(LoginRequiredMixin, generic.ListView):
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.prefetch_related('categories').filter(author=self.request.user)

class FavoritesView(
    LoginRequiredMixin,
    generic.ListView,
):
    model = Article
    context_object_name = 'articles'
    ordering = ['-created_at']

    def get_queryset(self):
        return Article.objects.prefetch_related('categories').filter(
            Q(author=self.request.user) & Q(favorites=True)
        )

class ToggleFavoriteView(LoginRequiredMixin, View):

    @method_decorator(require_POST)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk, author=self.request.user)
        article.favorites = not article.favorites
        article.save()
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
