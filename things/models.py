from django.db import models

class Thing():
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
