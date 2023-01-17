import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.parkinglot.models import ParkingLot, ParkingPlace
from apps.parkinglot.serializers import LotModelSerializer, PlaceModelSerializer


# Create your views here.

class GetParkingLotView(APIView):
    def get(self,request):
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
    def get(self,request):
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
        place_num = data.get('place_num')

        return Response({
            'code':200,
            'message':'success',
            'data':{
                'parkinglot_place_num':place_num
            }
        })

