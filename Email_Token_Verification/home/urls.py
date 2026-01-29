
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('home/', views.index, name='home'),
    path('verify/<str:token>/', views.verify, name='verify'),
]
