from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from .models import Employee


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