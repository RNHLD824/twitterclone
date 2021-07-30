from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class AllTweets(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is the page where we can see all of the Tweets.')
    
    def post(self, request, *args, **kwargs):
        pass