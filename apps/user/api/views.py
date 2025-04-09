from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from ..models import *
# Create your views here.

def user_login(request):
    return HttpResponse("user_login")

class RegisterAPI(APIView):
    def post(self, request):
        user = User_Login(username="123456", password="1234567890")
        user.save()
        return Response({"message": "User registered successfully!"})

class LoginAPI(APIView):
    def post(self, request):
        user = User_Login.objects.get(username="123456")
        return Response({"message": f"User {user.username} logged in successfully!"})

class DeletAPI(APIView):
    def post(self, request):
        user = User_Login.objects.get(username="123456")
        user.delete()
        return Response({"message": "User deleted successfully!"})
class ChangeAPI(APIView):
    def post(self, request):
        user = User_Login.objects.get(username="123456")
        user.password = "9876543210"
        user.save()
        return Response({"message": "User password changed successfully!"})


class Querr(APIView):
    def post(self, request):
        users = User_Login.objects.all()
        users = [user.username for user in users]
        return Response({"message": f"Users:{users}"})

class ArticleAPI(APIView):
    def post(self, request):
        user = User_Login(username="fhajsdhflk", password="1234567890")
        user.save()
        article = Article(title="Article1", content="This is the content of the article", author=user)
        article.save()
        return Response({"message": "Article created successfully!"})