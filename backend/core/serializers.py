from rest_framework import serializers
from .models import School, DemandCategory, Demand
from users.models import Employee


class DemandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandCategory
        fields = ['id', 'name', 'description']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'city', 'inep_code', 'created_at']


class DemandSerializer(serializers.ModelSerializer):
    school_name = serializers.CharField(source='school.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    employee_name = serializers.SerializerMethodField()

    class Meta:
        model = Demand
        fields = ['id', 'school', 'school_name', 'category', 'category_name',
                  'description', 'status', 'employee', 'employee_name',
                  'created_at', 'updated_at']
        read_only_fields = ['employee', 'school', 'status', 'created_at', 'updated_at']

    def get_employee_name(self, obj):
        return obj.employee.user.get_full_name() or obj.employee.user.username


class DemandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = ['category', 'description']

    def validate_category(self, value):
        if not DemandCategory.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Categoria não existe.")
        return value

    def create(self, validated_data):
        employee = Employee.objects.get(user=self.context['request'].user)
        return Demand.objects.create(
            employee=employee,
            school=employee.school,
            **validated_data
        )


class DemandExportSerializer(serializers.ModelSerializer):
    escola = serializers.CharField(source='school.name')
    categoria = serializers.CharField(source='category.name')
    funcionario = serializers.SerializerMethodField()
    email_funcionario = serializers.EmailField(source='employee.user.email')

    class Meta:
        model = Demand
        fields = ['escola', 'categoria', 'status', 'funcionario',
                  'email_funcionario', 'description', 'created_at', 'updated_at']

    def get_funcionario(self, obj):
        return obj.employee.user.get_full_name() or obj.employee.user.username