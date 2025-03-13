from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import User, FriendshipRequest
from .forms import UserRegistrationForm
from django.db.models import Q


class UserListView(generic.ListView):
    model = User
    template_name = 'sn/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            qs = qs.filter(
                Q(username__icontains=search_query)
            )

        return qs


class RegisterView(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        if username:
            user = get_object_or_404(User, username=username)
            return user
        else:
            return self.request.user


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['username', 'email', 'bio', 'avatar']
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def friends_request(request):
    friend_requests = FriendshipRequest.objects.filter(to_user=request.user)
    return render(request, 'users/friends_request.html', {'friend_requests': friend_requests})


@login_required
def send_friend_request(request, username):
    to_user = get_object_or_404(User, username=username)
    FriendshipRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
    return redirect('user-list')


@login_required
def accept_friend_request(request, pk, from_user):
    request.user.friends.add(from_user)
    delete_friend_request(request, pk)
    return redirect('friend-requests')


@login_required
def unfriend(request, pk):
    request.user.friends.remove(pk)
    return redirect('profile')


@login_required
def delete_friend_request(request, pk):
    friend_request = get_object_or_404(FriendshipRequest, pk=pk)
    friend_request.delete()
    return redirect('friend-requests')
