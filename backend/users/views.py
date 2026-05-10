from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Employee
from .serializers import LoginSerializer, EmployeeSerializer, EmployeeCreateSerializer


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if not user:
            return Response(
                {'detail': 'Credenciais inválidas'},
                status=401
            )
        refresh = RefreshToken.for_user(user)
        profile = 'admin' if user.is_staff else 'funcionario'
        school_id = None
        try:
            emp = Employee.objects.get(user=user)
            school_id = emp.school_id
        except Employee.DoesNotExist:
            pass
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'profile': profile,
            'school_id': school_id,
        })


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.select_related('user', 'school').all()

    def get_serializer_class(self):
        if self.action == 'create':
            return EmployeeCreateSerializer
        return EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.save()
        return Response(
            EmployeeSerializer(employee).data,
            status=201
        )