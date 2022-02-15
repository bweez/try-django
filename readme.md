# Learn Django tutorial

## Purpose

I am learning Django. This is a practice project.

## Reference Guides

- [Try Django 3.2 Playlist - YouTube](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL)
- [Try Django 3.2 Deploy to Digital Ocean](https://kirr.co/cv0e81)

### Activate a virtual env in the current directory for Mac

```bash
source bin/activate
```

### Run tests

```bash
python manage.py test
```

### Run server locally

```bash
python manage.py runserver
```

### Generate a Django Secret Key

Here is a one-liner that can be run from the cli.

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())
```

### Run Migrations to Add or Update DB models

```bash
# create new migrations based on model changes
python manage.py makemigrations
# then run migrations
python manage.py migrate
```

### Deploy to Digital Ocean

[Reference blog post](https://www.codingforentrepreneurs.com/blog/deploy-django-to-digitalocean-app-platform)
