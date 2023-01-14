from django.db import models

from apps.utils.base_model import BaseModel


# Create your models here.
class ParkingLot(BaseModel):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400, null=False)
    hourPrice = models.FloatField()
    monthPrice = models.FloatField()
    d = models.IntegerField(null=False)
    m = models.IntegerField(null=False)
    s = models.IntegerField(null=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'ParkingLot'
        verbose_name = 'ParkingLot'
        verbose_name_plural = 'ParkingLot'

