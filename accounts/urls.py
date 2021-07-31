from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path ('', views.Login.as_view(), name='login'),
    path ('register/', views.Register.as_view(), name='register'),
    path ('registration-success/', views.RegistrationSuccess.as_view(), name='registration-success'),
    path ('logout/', views.logoutUser, name='logout'),
]