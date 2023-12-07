from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.TextField(max_length=30, unique=True)
    description = models.TextField(max_length=30)
    quantity = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ])
