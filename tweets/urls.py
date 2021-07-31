from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path ('all-tweets/', views.AllTweets.as_view(), name='all-tweets'),
]