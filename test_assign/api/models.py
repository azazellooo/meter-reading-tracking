import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Meter(models.Model):
    """счетчик"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400)
    person = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="meters"
    )
    current_meter_reading = models.IntegerField()


class History(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    meter = models.ForeignKey(to=Meter, on_delete=models.CASCADE, related_name='history')
    meter_reading = models.IntegerField()
    consumption = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])

# Create your models here.
