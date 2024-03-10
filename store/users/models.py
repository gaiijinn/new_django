from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now
# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True) #для уникального идентификатора
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True) #каждый раз при создании модели автоматически заполняется поле
    expiration = models.DateTimeField() #время действие ссылки будем считать

    def __str__(self):
        return f"Email verification object for {self.user.email}"

    def send_verif_email(self):
        link = reverse('users:verify', kwargs={'email': self.user.email, 'code': self.code})
        verif_link = f'{settings.DOMAIN_NAME}{link}' #+host
        subject = f'Подтверждение учетной записи {self.user.username}'
        message = f'Для подтверждения учетной записи {self.user.username} перейдите по ссылке {verif_link}'
        send_mail(
            subject=subject,
            message=message,
            from_email="from@example.com",
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False