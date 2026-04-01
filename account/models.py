from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='images/users/')
    phone_number = models.PositiveIntegerField()

