from rest_framework import serializers

from apps.orders.models import Orders


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        # fields = ['id','first_name']
        # exclude = ['id']