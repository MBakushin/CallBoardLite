from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from .services.utils import unique_slugify


User = get_user_model()


class Announce(models.Model):
    header = models.CharField(max_length=156)
    text = CKEditor5Field(config_name='extends')
    slug = models.CharField(max_length=156, blank=True, unique=True)
    time_to_create = models.DateTimeField(auto_now_add=True)
    time_to_update = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author_announces')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='announces')
    # respond = models.ForeignKey('Respond', on_delete=models.CASCADE)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('announce_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.header)
        super().save(*args, **kwargs)


class Category(models.Model):
    CATEGORIES = [('tanks', 'Tanks'), ('healers', 'Healers'), ('dd', 'DD'),
                  ('traders', 'Traders'), ('guildmasters', 'Guildmasters'),
                  ('questgivers', 'Questgivers'), ('blacksmiths', 'Blacksmiths'),
                  ('leatherworkers', 'Leatherworkers'),
                  ('potion_masters', 'Potions Masters'),
                  ('spellmasters', 'Spellmasters')]

    title = models.CharField(max_length=56, choices=CATEGORIES, default='tanks')
    slug = models.SlugField(max_length=56, blank=True)

    announce = models.ForeignKey('Announce', null=True, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Respond(models.Model):
    header = models.CharField(max_length=256)
    time_to_create = models.DateTimeField(auto_now_add=True)
    time_to_update = models.DateTimeField(auto_now=True)

    announce = models.ForeignKey('Announce', on_delete=models.CASCADE, related_name='responds')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_responds')

    def __str__(self):
        return f'{self.author}:{self.header}'
