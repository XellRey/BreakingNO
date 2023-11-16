from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import CustomUserCreationForm, LoginForm


# Create your views here.


class login_view(LoginView):
    authentication_form = LoginForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('statements')


def sign_up(request):

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('statements')
    form = CustomUserCreationForm
    return render(request, 'registration/signup.html', context={"register_form": form})
