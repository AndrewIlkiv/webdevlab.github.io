from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Order(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title, self.description, self.price
