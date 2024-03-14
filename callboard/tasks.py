from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from config import settings
from callboard.models import Respond


@shared_task
def send_notification(slug, header_announce, header_respond, email):
    html_context = render_to_string(
        'respond_created_email.html',
        {'header_announce': header_announce,
         'header_respond': header_respond,
         'link': f'{settings.SITE_URL}/announce/slug/'}
    )

    msg = EmailMultiAlternatives(
        subject=header_respond,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )

    msg.attach_alternative(html_context, 'text/html')
    msg.send()
