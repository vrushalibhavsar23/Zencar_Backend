from rest_framework import serializers
from .models import Employees
from django.contrib.auth import authenticate
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'mobile_no', 'date_of_birth', 'location')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        employee = Employees.objects.create_user(**validated_data)
        return employee
    

class EmployeeLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("User account is disabled.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        return data
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
        
