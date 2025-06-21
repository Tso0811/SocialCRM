from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    line_id = models.CharField(max_length=64, null=True, blank=True, unique=True)
