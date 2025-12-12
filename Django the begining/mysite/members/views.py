from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
# This is where we gather the information we need to send back a proper response. 


def members(request):
    mymembers = Member.objects.all().values() # .values() converts each row into a python dictionary instead of a model instance
    template = loader.get_template('myfirst.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('main.html')
    context = {
        'x':['Apple','Banana','Cherry'],
        'y':['Apple','Banana','Cherry'],
    }
    return HttpResponse(template.render(context, request))

def search(request):
    # kept for backward compatibility but not used by template anymore
    mydata = Member.objects.none()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        if firstname:
            mydata = Member.objects.filter(firstname__icontains=firstname).values()
    return render(request, 'myfirst.html', {'data': mydata})
