from django.contrib import admin
from .models import School, DemandCategory, Demand


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'inep_code', 'created_at']
    search_fields = ['name', 'inep_code']


@admin.register(DemandCategory)
class DemandCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    list_display = ['school', 'category', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'category', 'school']
    search_fields = ['description', 'school__name', 'category__name']