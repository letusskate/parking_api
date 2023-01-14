import json

from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class AreaParkingLot(APIView):
    def get(self,request):
        data = json.loads(request.body)
        left_top_x = data['left-top-x']
        left_top_y = data['left-top-y']
        right_bottom_x = data['right-bottom-x']
        right_bottom_y = data['right-bottom-y']
