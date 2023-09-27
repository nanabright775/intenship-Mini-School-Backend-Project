from models import User
from log.logserializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

class YourModelViewSet(APIView.ModelViewSet):
    """api views for users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer