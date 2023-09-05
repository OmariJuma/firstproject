from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Homepage, Hi from Django</h1>")
# Create your views here.
def about_view(*args, **kwargs):
    return HttpResponse("<h1>About page: Hello there</h1>")
def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact page: Here is my contact 📞</h1>")