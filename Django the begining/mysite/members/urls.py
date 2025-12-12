from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    # search should have its own distinct path so it doesn't conflict with the members list
    path('members/search/', views.search, name='search'),

]
