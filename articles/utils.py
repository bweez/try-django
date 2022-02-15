from django.utils.text import slugify


def slugify_instance_title(instance, save=False):
    slug = slugify(instance.title)
    related_class = instance.__class__
    query = related_class.objects.filter(slug=slug).exclude(id=instance.id)
    if query.exists():
        slug = f"{slug}-{instance.id}"
    instance.slug = slug

    if(save):
        instance.save()

    return instance
