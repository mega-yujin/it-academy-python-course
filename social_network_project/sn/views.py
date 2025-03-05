from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404, render
from .models import Post, Hashtag, Comment
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.views.generic import UpdateView
from .forms import PostForm, CommentForm
import re


class PostListView(ListView):
    model = Post
    template_name = 'sn/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        search_query = self.request.GET.get('q')
        hashtag_filter = self.request.GET.get('hashtag')

        filter_user = get_object_or_404(User, username=self.kwargs.get('username'))
        qs = qs.filter(
            Q(author=filter_user)
        )

        if search_query:
            qs = qs.filter(
                Q(content__icontains=search_query)
            )

        if hashtag_filter:
            qs = qs.filter(hashtags__name__iexact=hashtag_filter.lower())

        return qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['hashtag_filter'] = self.request.GET.get('hashtag', '')

        context['popular_hashtags'] = Hashtag.objects.annotate(
            post_count=Count('post')
        ).order_by('-post_count')[:10]

        context['is_user_page'] = (
                self.request.user.is_authenticated and
                self.request.user.username == self.kwargs['username']
        )

        return context


class PostListViewRecent(ListView):
    model = Post
    template_name = 'sn/post_list_recent.html'
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        search_query = self.request.GET.get('q')
        hashtag_filter = self.request.GET.get('hashtag')

        if search_query:
            qs = qs.filter(
                Q(content__icontains=search_query) |
                Q(author__username__icontains=search_query)
            )

        if hashtag_filter:
            qs = qs.filter(hashtags__name__iexact=hashtag_filter.lower())

        return qs.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        context['hashtag_filter'] = self.request.GET.get('hashtag', '')

        context['popular_hashtags'] = Hashtag.objects.annotate(
            post_count=Count('post')
        ).order_by('-post_count')[:10]

        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'sn/post_form.html'

    def get_success_url(self):
        return reverse_lazy('post-list', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        self.process_hashtags(form.cleaned_data['hashtags'])
        return response

    def process_hashtags(self, hashtags_str):
        hashtags = re.findall(r'#(\w+)', hashtags_str)
        for tag in hashtags:
            hashtag, _ = Hashtag.objects.get_or_create(name=tag.lower())
            self.object.hashtags.add(hashtag)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'sn/post_update.html'

    def get_success_url(self):
        return reverse_lazy('post-list', kwargs={'username': self.request.user.username})

    def get_initial(self):
        initial = super().get_initial()
        initial['hashtags'] = ' '.join(f"#{tag.name}" for tag in self.object.hashtags.all())
        return initial

    def form_valid(self, form):
        self.object.hashtags.clear()
        self.process_hashtags(form.cleaned_data['hashtags'])
        return super().form_valid(form)

    def process_hashtags(self, hashtags_str):
        hashtags = re.findall(r'#(\w+)', hashtags_str)
        for tag in hashtags:
            hashtag, _ = Hashtag.objects.get_or_create(name=tag.lower())
            self.object.hashtags.add(hashtag)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'sn/post_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-list', kwargs={'username': self.request.user.username})

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post-list-recent')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            return redirect('post-list-recent')
    return redirect('post-list-recent')


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('post-list-recent')
    else:
        form = CommentForm(initial={'content': comment.content})

    return render(request, 'sn/comment_form.html', {
        'form': form,
        'comment': comment,
    })


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    post_author_username = comment.post.author.username
    comment.delete()
    return redirect('post-list-recent')
