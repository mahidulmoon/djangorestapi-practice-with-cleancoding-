from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    def articleLength(self):
        return len(self.title)

    def __str__(self):
        return self.title