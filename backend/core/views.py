from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
import csv
from io import StringIO
from .models import School, DemandCategory, Demand
from .serializers import (
    SchoolSerializer, DemandCategorySerializer,
    DemandSerializer, DemandCreateSerializer, DemandExportSerializer
)
from .filters import DemandFilter
from users.models import Employee


class DemandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DemandFilter
    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_staff:
            return Demand.objects.select_related('school', 'category', 'employee__user').all()
        emp = Employee.objects.get(user=self.request.user)
        return Demand.objects.filter(school=emp.school).select_related('school', 'category', 'employee__user')

    def get_serializer_class(self):
        if self.action == 'create':
            return DemandCreateSerializer
        return DemandSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            DemandSerializer(serializer.instance).data,
            status=status.HTTP_201_CREATED
        )


class MyDemandsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DemandSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DemandFilter
    pagination_class = None

    def get_queryset(self):
        emp = Employee.objects.get(user=self.request.user)
        return Demand.objects.filter(school=emp.school).select_related('school', 'category', 'employee__user')


class DemandExportCSVView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        demands = Demand.objects.select_related('school', 'category', 'employee__user').all()
        serializer = DemandExportSerializer(demands, many=True)
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=serializer.data[0].keys() if serializer.data else [])
        writer.writeheader()
        writer.writerows(serializer.data)
        response = HttpResponse(output.getvalue(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="demandas.csv"'
        return response


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DemandCategory.objects.all()
    serializer_class = DemandCategorySerializer