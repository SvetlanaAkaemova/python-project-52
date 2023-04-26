from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
