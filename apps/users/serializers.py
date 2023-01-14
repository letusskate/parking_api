#序列化，没规则转为有规则
from rest_framework import serializers

from apps.users.models import UserGender, Users


class CreateUserSerializer(serializers.Serializer):
    username = serializers.EmailField(
        max_length=200,allow_blank=False
    )
    password=serializers.CharField(
        max_length=200
    )
    first_name = serializers.CharField(
        max_length=200,
        error_messages={
            "blank":"first name is required",
            "max-length":"xxx"
        }
    )
    last_name = serializers.CharField(
        max_length=200
    )
    gender = serializers.ChoiceField(
        choices=[item.value for item in UserGender]
    )

    def validate(self,attrs):
        username = attrs.get('username')
        if Users.objects.filter(username = username).exists():
            raise serializers.ValidationError("User username exists")
        return attrs



class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        # fields = ['id','first_name']
        # exclude = ['id']