from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(Model):
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.PositiveIntegerField(
        default=0, 
        unique=False, 
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ])
