from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # Additional fields here

    def __str__(self):
        return self.username


# Create your models here.
