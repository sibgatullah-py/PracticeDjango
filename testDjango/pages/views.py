# View handles all our requests . Here we write all the logical stuff.views.py handles your various webpages
from django.shortcuts import render
from django.http import HttpResponse

def home_view(*args, **kwaegs):
    return HttpResponse('<h1>Hello World</h1>')

def contact_view(*args, **kweags):
    return HttpResponse('<h1>Contact Page</h1>')

def blog_view(*args, **kwargs):
    return HttpResponse('<h1>Blog Page</h1>')

def gallary_view(*args, **kwargs):
    return HttpResponse('<h1>Gallary Page</h1>')