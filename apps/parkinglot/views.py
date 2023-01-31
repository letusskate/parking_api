import json
import random

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.parkinglot.models import ParkingLot, ParkingPlace
from apps.parkinglot.serializers import LotModelSerializer, PlaceModelSerializer


# Create your views here.

class GetParkingLotView(APIView):
    def post(self,request):
        data = json.loads(request.body)
        lot_id = data.get('parkinglot_id')
        parkinglot = ParkingLot.objects.filter(id=lot_id)
        if not parkinglot.first():
            return JsonResponse({
                'code': 404,
                'message': 'Parkinglot not exist',
            })
        place = ParkingPlace.objects.filter(parkingLot_id=lot_id)
        lot_data = LotModelSerializer(parkinglot,many=True).data
        place_data = PlaceModelSerializer(place,many=True).data
        return Response({
            'code':200,
            'message':'success',
            'data':{
                'paringlot_data':lot_data[0],
                'parkingplace_data':place_data
            }
        })


class AreaParkingLotView(APIView):
    def post(self,request):
        data = json.loads(request.body)
        left_top_latitude = data.get('left-top-latitude')
        left_top_longitude = data.get('left-top-longitude')
        right_bottom_latitude = data.get('right-bottom-latitude')
        right_bottom_longitude = data.get('right-bottom-longitude')
        lot_queryset = ParkingLot.objects.get_queryset()
        lot_need = lot_queryset.filter(latitude__gte=right_bottom_latitude).filter(latitude__lte=left_top_latitude).filter(longitude__gte=left_top_longitude).filter(longitude__lte=right_bottom_longitude)
        lot_data = LotModelSerializer(lot_need,many=True).data
        return Response({
            'code':200,
            'message':'success',
            'data':{
                'parkinglot_data':lot_data
            }
        })

class AddParkingLotView(APIView):
    def post(self,request):
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description',name)
        hour_price = data.get('hour_price',random.randint(1,10))
        month_price = data.get('month_price',random.randint(hour_price*50,hour_price*300))
        latitude = data.get('latitude',0)
        longitude = data.get('longitude',0)
        spare_place_num = data.get('spare_place_num',random.randint(0,100))
        place_num = data.get('place_num',spare_place_num+random.randint(0,50))
        parkinglot = ParkingLot.objects.filter(name=name).first()
        if not parkinglot:
            parkinglot = ParkingLot.objects.create(
                name=name,
                description=description,
                hourPrice=hour_price,
                monthPrice=month_price,
                latitude=latitude,
                longitude=longitude,
            )
            identifier_set = set()
            while len(identifier_set)<place_num:
                strs=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
                identifier_set.add(strs[random.randint(0,25)]+str(random.randint(1,place_num)))
            cnt = 0
            pwd_all = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            for identifier in identifier_set:
                cnt+=1
                pwd = ''
                for i in range(6):
                    pwd += pwd_all[random.randint(0,9)]
                if cnt<=spare_place_num:
                    ParkingPlace.objects.create(
                        identifier=identifier,
                        parkingLot_id=parkinglot.id,
                        spare=True,
                        password=pwd
                    )
                else:
                    ParkingPlace.objects.create(
                        identifier=identifier,
                        parkingLot_id=parkinglot.id,
                        spare=False,
                        password=pwd
                    )
        id = parkinglot.id
        return Response({
            'code':200,
            'message':'success',
            'data':{
                'parkinglot_id':id,
                'parkinglot_spare_place_num':spare_place_num,
                'parkinglot_place_num':place_num,
                'parkinglot_hour_price':hour_price,
                'parkinglot_month_price':month_price
            }
        })

