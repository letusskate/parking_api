from rest_framework import serializers

from apps.parkinglot.models import ParkingLot, ParkingPlace


class LotModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLot
        # fields = '__all__'
        # fields = ['id','first_name']
        exclude = ['created_at','updated_at',"format_created_at","format_updated_at"]

class PlaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingPlace
        # fields = '__all__'
        # fields = ['id','first_name']
        exclude = ['created_at', 'updated_at', "format_created_at", "format_updated_at"]