from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Library(models.Model):
    owner = models.OneToOneField(User, related_name="library", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
