from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class TwitterUser(AbstractUser):
    followers = models.ManyToManyField("self", symmetrical=False)
