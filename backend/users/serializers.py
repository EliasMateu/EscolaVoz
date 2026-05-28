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


class EmployeeCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=6)
    school_id = serializers.IntegerField(write_only=True)
    is_admin = serializers.BooleanField(write_only=True, default=False)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password', 'school_id', 'role', 'is_admin']

    def create(self, validated_data):
        is_admin = validated_data.pop('is_admin', False)
        school_id = validated_data.pop('school_id')
        school = None
        if school_id:
            from core.models import School
            school = School.objects.get(id=school_id)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        if is_admin:
            user.is_staff = True
            user.save()
        return Employee.objects.create(user=user, school=school, **validated_data)