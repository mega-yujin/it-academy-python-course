from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.models import User

# Create your views here.


def article_list(request):
    article = Article.objects.all()
    return render(request, 'news/article_list.html', {'articles': article})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    users = User.objects.all()
    # User.objects.save(username='Bob', password='1234')
    return render(request, 'news/add_article.html', {'form': form, 'users': users})


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'news/delete_article.html', {'article': article})
