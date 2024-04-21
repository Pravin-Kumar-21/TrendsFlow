from django.shortcuts import render, redirect
from django.contrib.auth import logout
from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, DetailView, UpdateView
from django.views import View
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from . import mixins


def index(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return redirect("/")


class LoginView(mixins.LoggedOutOnlyView, FormView):
    template_name = "login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")
