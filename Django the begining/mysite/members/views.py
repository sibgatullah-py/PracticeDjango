from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# This is where we gather the information we need to send back a proper response. 

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))