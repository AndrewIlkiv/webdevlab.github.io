from django.db import models


class Order(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title, self.description, self.price
