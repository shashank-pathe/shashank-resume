from django.db import models

# Create your models here.

class Mail(models.Model):
    name= models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=900)


class Documents(models.Model):
    cource= models.CharField(max_length=200)
    univercity= models.CharField(max_length=200)
    classs= models.CharField(max_length=200)
    subject= models.CharField(max_length=200)
    document= models.ImageField()
 