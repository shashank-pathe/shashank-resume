from django.db import models

# Create your models here.

class Mail(models.Model):
    name= models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=900)


 