from .models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def auto_token_creating(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        Token.objects.create(user=instance)
