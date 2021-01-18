from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  pref_name = models.CharField(max_length =40)
