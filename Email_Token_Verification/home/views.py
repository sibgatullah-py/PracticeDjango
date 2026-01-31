from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm
from .utils import *
from django.contrib.auth.models import User



from .models import *
import uuid # to generate token



def index(request):
    return render(request, 'home/index.html')


def signup_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username=email).exists():
                return HttpResponse("User already exists")

            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            
            user.is_active= False

            profile = Profile.objects.create(
                user=user,
                email_token=str(uuid.uuid4())
            )
            print("EMAIL FUNCTION CALLED")


            send_email_token(email, profile.email_token)
            return HttpResponse("Check your email for verification link")

    else:
        form = LoginForm()

    return render(request, "home/form.html", {"form": form})
        
    
def verify(request, token):
    try:
        obj = Profile.objects.get(email_token=token)
        
        if obj.is_verified:
            return HttpResponse("Already verified")
        
        obj.is_verified = True
        obj.user.is_active = True
        obj.save()
        return redirect('home')

    except Profile.DoesNotExist:
        return HttpResponse('Invalid Token')