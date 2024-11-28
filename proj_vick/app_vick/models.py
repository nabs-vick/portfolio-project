from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField( max_length=50)
    Email = models.EmailField( max_length=254)
    Phone_Number = models.IntegerField()
    Message = models.CharField( max_length=50)
