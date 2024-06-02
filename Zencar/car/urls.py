from django.urls import path
from .views import *

urlpatterns = [
    path('inventory/', CarInventoryListCreateView.as_view(), name='car-inventory-list-create'),
    path('sales/', CarSalesListCreateView.as_view(), name='car-sales-list-create'),
    path('upload-inventory/', UploadCarInventoryExcelView.as_view(), name='upload-car-inventory'),
    path('upload-sales/', UploadCarSalesExcelView.as_view(), name='upload-car-sales'),
    path('inventory-years/', inventory_years, name='inventory_years'),
    path('sales-years/', sales_years, name='sales_years'),
]