from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import School, DemandCategory
from .serializers import SchoolSerializer, DemandCategorySerializer


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DemandCategory.objects.all()
    serializer_class = DemandCategorySerializer