from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    model = models.CharField(max_length=10)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

