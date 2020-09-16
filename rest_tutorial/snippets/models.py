from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=50)
    created = models.TimeField( auto_now_add=True)