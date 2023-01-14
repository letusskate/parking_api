from enum import IntEnum

from django.db import models

from apps.parkinglot.models import ParkingPlace
from apps.users.models import Users
from apps.utils.base_model import BaseModel


# Create your models here.
class OrdersKind(IntEnum):
    pre = 0
    parking = 1
    paying = 2
    finish = 3
    @classmethod
    def choices(cls):
        return tuple(((item.value, item.name) for item in cls))
class Orders(BaseModel):
    status = models.SmallIntegerField(choices=OrdersKind.choices())
    parkingBeginTime = models.FloatField(default=0, null=True, blank=True)
    parkingEndTime = models.FloatField(default=0, null=True, blank=True)
    parkingPlace = models.ForeignKey(ParkingPlace, related_name='parkingPlace_order', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Users, related_name='user_order', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return "order of "+self.user.first_name+self.user.last_name
    class Meta:
        db_table = 'Orders'
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'
