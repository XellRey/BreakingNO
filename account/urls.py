import django.contrib.auth.views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signin/', views.login_view.as_view(), name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
    ]
