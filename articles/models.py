from django.db import models
from django.db.models.signals import pre_save, post_save
# Create your models here.
from .utils import slugify_instance_title
# Model field docs - https://docs.djangoproject.com/en/4.0/ref/models/fields/


class Article(models.Model):
    title = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return f'/articles/{self.slug}/'

    # creating an override for the save method on models
    def save(self, *args, **kwargs):
        # Moving into a pre-save signal
        # Creating an override:
        # do something here
        # not necessarily the best way to manage this behavior
        # there may be instances where we don't want to do this in `save()`
        # if(self.slug is None):
        #     self. slug = slugify(self.title)
        # call the original save to preserve the behavior of `save()`
        super().save(*args, **kwargs)


# These functions are for capturing the model pre or post it is is saved method call.
# It creates a signal that can be operated on.


def article_pre_save(sender, instance, *args, **kwargs):
    # print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    # print('post_save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Article)
