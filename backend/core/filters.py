import django_filters
from .models import Demand


class DemandFilter(django_filters.FilterSet):
    school_id = django_filters.NumberFilter(field_name='school__id')
    category_id = django_filters.NumberFilter(field_name='category__id')
    status = django_filters.ChoiceFilter(choices=Demand.STATUS_CHOICES)
    created_after = django_filters.DateFilter(field_name='created_at__date', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='created_at__date', lookup_expr='lte')

    class Meta:
        model = Demand
        fields = ['school_id', 'category_id', 'status', 'created_after', 'created_before']