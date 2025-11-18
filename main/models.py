from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django import forms

# Create your models here.
import uuid
from django.db import models
from django.contrib.humanize.templatetags.humanize import intcomma

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('jacket', 'Jacket'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('socks', 'Socks'),
        ('accessories', 'Accessories'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')


    product_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.product_views > 20
    
    def increment_views(self):
        self.product_views += 1
        self.save(update_fields=["product_views"])
    
    def delete_product(self):
        self.delete()
    
    def price_style(self):
        return f"Rp {intcomma(self.price)}"
    
class Car(models.Model):

    name = forms.CharField(max_length=255)
    brand = forms.CharField(max_length=255)
    stock = forms.IntegerField()







 
    