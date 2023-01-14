import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.orders.models import Orders
from apps.orders.serializers import OrderModelSerializer
from apps.parkinglot.models import ParkingLot, ParkingPlace
from apps.users.models import Users


# Create your views here.
class ReservationView(APIView):
    def post(self,request):
        data = json.loads(request.body)
        parkinglot_id = data['parkinglot']
        username = data['username']
        queryset = ParkingPlace.objects.all()
        queryset = queryset.filter(parkingLot_id=parkinglot_id)
        parkingplace = queryset.filter(spare=True).first()
        if not parkingplace:
            return JsonResponse({
                'code': 404,
                'message': 'No place now',
            })
        ParkingPlace.objects.filter(id=parkingplace.id).update(spare=False)
        order = Orders.objects.create(
            status=0,
            parkingBeginTime=0,
            parkingEndTime=0,
            parkingPlace_id=parkingplace.id,
            user=Users.objects.filter(username=username).first()
        )
        return JsonResponse({
            'code':200,
            'message':'success',
            'data':{
                'order_id':order.id,
                'parkinglot_id':parkinglot_id,
                'parkingplace_id':parkingplace.id,
                'parkingplace_identifier':parkingplace.identifier
            }
        })

class DeleteReservationView(APIView):
    def post(self,request):
        data = json.loads(request.body)
        order_id = data['order_id']
        order = Orders.objects.filter(id=order_id)
        if not order.first():
            return JsonResponse({
                'code': 404,
                'message': 'Order not exist',
            })
        if order.first().status!=0:
            return JsonResponse({
                'code': 404,
                'message': 'not a reservation',
            })
        ParkingPlace.objects.filter(id=order.first().parkingPlace.id).update(spare=True)
        order.delete()
        return JsonResponse({
            'code':200,
            'message':'success'
        })

class GetOrderView(APIView):
    def get(self,request):
        data = json.loads(request.body)
        order_id = data['order_id']
        order = Orders.objects.filter(id=order_id)
        if not order.first():
            return JsonResponse({
                'code': 404,
                'message': 'Order not exist',
            })
        order_data = OrderModelSerializer(order,many=True).data
        return Response({
            'code':200,
            'message':'success',
            'data':order_data[0]
        })
class GetUserOrdersView(APIView):
    def get(self,request):
        data = json.loads(request.body)
        username = data['username']
        user = Users.objects.filter(username=username).first()
        if not user:
            return JsonResponse({
                'code': 404,
                'message': 'User not exist',
            })
        user_id = user.id
        orders = Orders.objects.filter(user_id=user_id)
        orders_data = OrderModelSerializer(orders,many=True).data
        return Response({
            'code':200,
            'message':'success',
            'data':{
                'list':orders_data
            }
        })

