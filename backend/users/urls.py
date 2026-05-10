from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
] + router.urls