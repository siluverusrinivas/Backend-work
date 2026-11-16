from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .models import User


class RegisterUserView(APIView):
    def post(self,request):
        name=request.data.get('name')
        email=request.data.get('email')
        password=request.data.get('password')

        # basic validation
        if not name or not email or not password:
            return Response(
            {
                "message":"name,email and password are required"
            },
            status=status.HTTP_400_BAD_REQUEST
        )


        # check email exist

        if User.objects.filter(email=email).exists():
            return Response(
                {
                    "error":"email already exist"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user=User.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )

        return Response(
            {
                "message":"user registered succcessfully",
                "user":{
                    "id":user.id,
                    "name":user.name,
                    "email":user.email
                }

            },
            status=status.HTTP_201_CREATED
        )

class ListUserView(APIView):
    def get(self,request):
        users=User.objects.all().order_by('_created_at')

        user_list=[]

        for user in users:
            user_list.append({
                'id':user.id,
                'name':user.name,
                'email':user.email,
                'created_at':user.created_at
            })
        return Response (
            {
                "message":"user list fetched successfully",
                "count":len(user_list),
                'users':user_list
            },
            status=status.HTTP_200_OK
        )