from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),
    path('statements/', views.statements, name='statements'),
    path('statements/create/', views.create_st, name='create'),
    path('profile/', views.profile, name='profile'),

    path('_admin/statements/', views.admin_int, name='admin_int'),
    path('_admin/statemnt/detail/<pk>/', views.st_detail, name='st_detail'),

    path('_admin/statemnt/<operation>/<pk>/', views.accept_decline_st, name='accept')
]