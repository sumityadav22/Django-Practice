from django.db import models

# Create your models here.

class News(models.Model):
    auther = models.CharField(max_length = 30)
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 40)

#This is how we can 
def __str__(self):
    return self.title