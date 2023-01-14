from django.db import models

from apps.parkinglot.models import ParkingLot
from apps.utils.base_model import BaseModel


# Create your models here.
class ParkingPlace(BaseModel):
    identifier = models.CharField(max_length=200,null=False)
    parkingLot = models.ForeignKey(ParkingLot, related_name='parkingLot_parkingPlace', on_delete=models.CASCADE)
    spare = models.BooleanField(default=True)
    def __str__(self):
        return self.identifier
    class Meta:
        db_table = 'ParkingPlace'
        verbose_name = 'ParkingPlace'
        verbose_name_plural = 'ParkingPlace'
