from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Employees
from .serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token



class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'token': token.key
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)