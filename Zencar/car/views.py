from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarInventory, CarSales
from .serializers import CarInventorySerializer, CarSalesSerializer
from rest_framework.parsers import MultiPartParser, FormParser
import pandas as pd
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

class CarInventoryListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CarInventory.objects.all()
    serializer_class = CarInventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_year']
    # permission_classes = [AllowAny]
    

class CarSalesListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CarSales.objects.all()
    serializer_class = CarSalesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_year']

class UploadCarInventoryExcelView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        df = pd.read_excel(file_obj)
        for _, row in df.iterrows():
            CarInventory.objects.update_or_create(
                car_name=row['car_name'],
                model_year=row['model_year'],
                defaults={'quantity': row['quantity']}
            )
        return Response(status=status.HTTP_200_OK)

class UploadCarSalesExcelView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.data['file']
        df = pd.read_excel(file_obj)
        for _, row in df.iterrows():
            CarSales.objects.update_or_create(
                car_name=row['car_name'],
                model_year=row['model_year'],
                defaults={'sales_count': row['sales_count']}
            )
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET'])
def inventory_years(request):
    years = CarInventory.objects.order_by('model_year').values_list('model_year', flat=True).distinct()
    return Response(years)

@api_view(['GET'])
def sales_years(request):
    years = CarSales.objects.order_by('model_year').values_list('model_year', flat=True).distinct()
    return Response(years)
