from django.db import models

# Create your models here.

# Model field docs - https://docs.djangoproject.com/en/4.0/ref/models/fields/


class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
