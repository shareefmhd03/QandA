from django.utils.text import slugify
import string
import random


def random_string(n):
    rand_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k = n))
    return rand_string

def slug_generator(text):
    new_slug = slugify(text)
    from . models import Blog
    if Blog.objects.filter(slug = new_slug).exists():
        return slug_generator(text + random_string(5))
    return new_slug 


