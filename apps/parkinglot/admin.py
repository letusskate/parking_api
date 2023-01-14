from django.contrib import admin

from apps.parkinglot.models import ParkingLot, ParkingPlace

# Register your models here.

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'hourPrice', 'monthPrice', 'latitude','longitude']

@admin.register(ParkingPlace)
class ParkingPlaceAdmin(admin.ModelAdmin):
    fields = ['identifier','parkingLot','spare']