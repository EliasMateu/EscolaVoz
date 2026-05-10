from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    inep_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'schools'
        ordering = ['name']

    def __str__(self):
        return self.name


class DemandCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'demand_categories'
        verbose_name_plural = 'Demand Categories'

    def __str__(self):
        return self.name


class Demand(models.Model):
    STATUS_CHOICES = [
        ('open', 'Aberta'),
        ('in_progress', 'Em Andamento'),
        ('resolved', 'Resolvida'),
        ('rejected', 'Rejeitada'),
    ]

    employee = models.ForeignKey('users.Employee', on_delete=models.CASCADE, related_name='demands')
    school = models.ForeignKey('core.School', on_delete=models.CASCADE, related_name='demands')
    category = models.ForeignKey(DemandCategory, on_delete=models.CASCADE, related_name='demands')
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'demands'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.category.name} - {self.school.name} ({self.status})"