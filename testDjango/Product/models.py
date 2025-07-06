from turtle import title
from django.db import models
#ORM = Object-Relation Mapper
#models.Model is actually a built in ORM class and Products here is it's child class inheriting 
class Products(models.Model):
    # these are fields in database 
    title   = models.CharField(max_length=60)
    details = models.TextField(default = 'This is cool!')
    price   = models.DecimalField(decimal_places=3,max_digits=10000)
    summery = models.TextField(blank = True)
    
