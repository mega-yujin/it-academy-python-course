from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View, generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login

from .forms import UserRegistrationForm


class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
