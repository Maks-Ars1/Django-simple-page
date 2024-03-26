from pickle import FALSE
from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    def __str__(self) -> str:
        return self.username

class Task(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)