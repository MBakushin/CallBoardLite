from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Announce(models.Model):
    header = models.CharField(max_length=156)
    text = CKEditor5Field()
    time_to_create = models.DateTimeField(auto_now_add=True)
    time_to_update = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ManyToManyField('Category')

    def __str__(self):
        return self.header


class Category(models.Model):
    CATEGORIES = [('tanks', 'Tanks'), ('healers', 'Healers'), ('dd', 'DD'),
                  ('traders', 'Traders'), ('guildmasters', 'Guildmasters'),
                  ('questgivers', 'Questgivers'), ('blacksmiths' , 'Blacksmiths'),
                  ('leatherworkers', 'Leatherworkers'),
                  ('potion_masters', 'Potions Masters'),
                  ('spellmasters', 'Spellmasters')]

    title = models.CharField(max_length=56, choices=CATEGORIES)

    # announ = models.ManyToManyField('Announce')

    def __str__(self):
        return self.title


class Respond(models.Model):
    header = models.CharField(max_length=256)

    announ = models.ForeignKey('Announce', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
