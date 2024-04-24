from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
import uuid
from users.models import User, EmailVerification


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    verif = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    verif.send_verif_email()  # from models def

