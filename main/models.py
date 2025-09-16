from django.db import models

# Create your models here.
import uuid
from django.db import models

class News(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('jacket', 'Jacket'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('socks', 'Socks'),
        ('accessories', 'Accessories'),
    ]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    news_views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def is_news_hot(self):
        return self.news_views > 20
    
    def increment_views(self):
        self.news_views += 1
        self.save(update_fields=["news_views"])
    
    def delete_product(self):
        self.delete()

 
    