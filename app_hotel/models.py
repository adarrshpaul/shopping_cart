from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(default='')

class Menu(models.Model):
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True, default=1)


