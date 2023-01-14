import time
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import Users
import json
from apps.users.serializers import CreateUserSerializer
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def get_userinfo(request):
    user = Users.objects.get(id=1)
    # print(user)
    result = render(request, 'userinfo.html', context={
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
    })
    return result

class RegisterView(APIView):
    authentication_classes = ()
    def post(self,request):
        import json
        user_data = json.loads(request.body)
        serializer=CreateUserSerializer(data={
            "username":user_data.get("username"),
            "password": user_data.get("password"),
            "first_name":user_data.get("first_name"),
            "last_name":user_data.get("last_name"),
            "gender":user_data.get("gender"),
        })
        if not serializer.is_valid():
            return Response(serializer.errors)
        # create方法
        user = Users.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            username=user_data['username'],
            gender=user_data['gender'],
            password=user_data['password']
        )

        cache.delete('user_data')#旁路模式，删除缓存

        # 创建用户
        return JsonResponse({'code': 200, 'message': 'success', "data": {
            "userId": user.id
        }})


class UserLoginView(APIView):
    authentication_classes = ()#不再token校验
    def post(self,request):
        data = json.loads(request.body)
        username = data.get('username')
        pswd = data.get('password')
        user = Users.objects.filter(username=username).first()
        if not user:
            return JsonResponse({
                'code': 404,
                'message': "User data not exist"
            })
        pswd = make_password(pswd)
        # if user.password!=pswd:
        if not check_password(user.password,pswd):
            return JsonResponse({
                'code': 404,
                'message': "User password not correct"
            })
        payload = {
            "username": username,
            # "exp":int(time.time())+30*60,
            "exp": int(time.time()) + 300000 * 60,
        }
        from django.conf import settings
        import jwt
        secret_key = settings.SECRET_KEY
        token = jwt.encode(payload, secret_key, algorithm='HS256').decode('utf-8')
        return JsonResponse({
            'code': 200,
            'message': 'success',
            'data': {
                'token': token
            }
        })


class ChangePasswordView(APIView):
    # authentication_classes = ()
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        pswd = data.get('password')
        npswd = data.get('new-password')
        _user = Users.objects.filter(username=username)
        user=_user.first()
        if not user:
            return JsonResponse({
                'code': 404,
                'message': "User data not exist"
            })
        if user.password!=pswd:
            return JsonResponse({
                'code': 404,
                'message': "User password not correct"
            })
        if pswd==npswd:
            return JsonResponse({
                'code': 404,
                'message': "two password is the same"
            })
        _user.update(password=npswd)
        # Users.objects.filter(email=email).update(password=npswd) #又查一遍很浪费时间
        return JsonResponse({
            'code':200,
            'message': 'success',
            'new-password': npswd
        })

class GetMoneyView(APIView):
    def get(self,request):
        data = json.loads(request.body)
        usr = Users.objects.filter(username=data["username"]).first()
        if not usr:
            return JsonResponse({
                'code':404,
                'message': 'user not exist',
            })
        money = usr.money
        return JsonResponse({
            'code':200,
            'message': 'success',
            'money': money
        })
class AddMoneyView(APIView):
    def post(self,request):
        data = json.loads(request.body)
        money = data['money']
        username = data['username']
        totalmoney = Users.objects.filter(username=username).first().money+money
        usr = Users.objects.filter(username=username).first()
        if not usr:
            return JsonResponse({
                'code':404,
                'message': 'user not exist',
            })
        Users.objects.filter(username=username).update(money=totalmoney)
        return JsonResponse({
            'code':200,
            'message':'success',
            'data':{
                'addmoney':money,
                'totalmoney':totalmoney
            }
        })
