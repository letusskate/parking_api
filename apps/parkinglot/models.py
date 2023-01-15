from django.db import models

from apps.utils.base_model import BaseModel


# Create your models here.
class ParkingLot(BaseModel):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400, null=False)
    hourPrice = models.FloatField()
    monthPrice = models.FloatField()
    latitude = models.FloatField(default=0,null=False)
    longitude = models.FloatField(default=0,null=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'ParkingLot'
        verbose_name = 'ParkingLot'
        verbose_name_plural = 'ParkingLot'

class ParkingPlace(BaseModel):
    identifier = models.CharField(max_length=200,null=False)
    parkingLot = models.ForeignKey(ParkingLot, related_name='parkingLot_parkingPlace', on_delete=models.CASCADE)
    spare = models.BooleanField(default=True)
    password = models.CharField(max_length=200,null=False,default='123456')
    def __str__(self):
        return self.identifier
    class Meta:
        db_table = 'ParkingPlace'
        verbose_name = 'ParkingPlace'
        verbose_name_plural = 'ParkingPlace'
