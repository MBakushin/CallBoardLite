from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from config import settings
from callboard.models import Respond
from callboard.tasks import send_notification


@receiver(post_save, sender=Respond)
def notify_about_respond(sender, instance, **kwargs):
    announce = instance.announce

    send_notification.delay(announce.slug, announce.header, announce.responds.last().header, announce.author.email)
