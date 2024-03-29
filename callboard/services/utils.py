import os
from datetime import datetime
from urllib.parse import urljoin
from django.core.files.storage import FileSystemStorage
from config import settings
from uuid import uuid4
from pytils.translit import slugify


def unique_slugify(instance, slug):
    """
    This func generates unique slug for a given instance
    if there is no slug
    """
    model = instance.__class__
    unique_slug = slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug


class CkeditorCustomStorage(FileSystemStorage):
    """
    Custom storage for Ckeditor
    """
    def get_folder_name(self):
        return datetime.now().strftime('%Y/%m/%d')

    def get_valid_name(self, name):
        return name

    def _save(self, name, content):
        folder_name = self.get_folder_name()
        name = os.path.join(folder_name, self.get_valid_name(name))
        return super()._save(name, content)

    location = os.path.join(settings.MEDIA_ROOT, 'uploads/')
    base_url = urljoin(settings.MEDIA_URL, 'uploads/')
