from django.db import models
from django.db.models import Avg

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    def get_products(self):
        return Product.objects.filter(category=self)
    
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, verbose_name="Category", on_delete= models.PROTECT)
    instagram = models.TextField(default='')
    def __obj__(self):
        return self