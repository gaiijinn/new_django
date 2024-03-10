from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
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
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            [self.user.email],
            fail_silently=False,
        )
