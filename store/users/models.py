from django.db import models
<<<<<<< HEAD

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='user_img', null=True, blank=True)

=======
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
>>>>>>> after_pause
