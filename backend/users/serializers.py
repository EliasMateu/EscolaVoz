from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class EmployeeSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_name = serializers.SerializerMethodField()
    school_name = serializers.CharField(source='school.name', read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'user_email', 'user_name', 'school_name', 'role', 'created_at']

    def get_user_name(self, obj):
        return obj.user.get_full_name() or obj.user.username