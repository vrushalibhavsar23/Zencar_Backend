from django.urls import path, include
from .views import *
urlpatterns = [
    path('register/', EmployeeCreateView.as_view(), name='employee-register'),
    path('login/', LoginAPIView.as_view(), name='employee-login'),
    # Include other app URLs here if needed
]