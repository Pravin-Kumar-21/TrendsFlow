from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    last_name = models.EmailField(max_length=100, blank=False)
    avatar = models.ImageField(upload_to="images")
    language = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.first_name
