# Learn Django tutorial

## Purpose

I am learning Django. This is a practice project. I have lots of notes and comments I generally would not leave in.

## Reference Guides

- [YouTube Playlist](https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL)
- [Deploy to Digital Ocean](https://kirr.co/cv0e81)

### Generate a Django Secret Key

Here is a one-liner that can be run from the cli.

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())
```