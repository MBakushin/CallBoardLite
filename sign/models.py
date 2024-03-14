from datetime import date, timedelta

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.urls import reverse

from callboard.services.utils import unique_slugify


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField(verbose_name='URL', max_length=128, blank=True, unique=True)
    image = models.ImageField(upload_to='profile_images/%Y/%m/%d', blank=True, default='profile_images/empty_avatar.jpg',
                              validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.user.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})
