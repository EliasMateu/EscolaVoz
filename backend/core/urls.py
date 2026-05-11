from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SchoolViewSet, CategoryViewSet, DemandViewSet,
    MyDemandsViewSet, DemandExportCSVView
)

router = DefaultRouter()
router.register(r'schools', SchoolViewSet, basename='school')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'demands', DemandViewSet, basename='demand')
router.register(r'demands/my', MyDemandsViewSet, basename='my-demand')

urlpatterns = [
    path('', include(router.urls)),
    path('demands/export/csv/', DemandExportCSVView.as_view(), name='demand-export-csv'),
]