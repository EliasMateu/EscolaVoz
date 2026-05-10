from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    school = models.ForeignKey('core.School', on_delete=models.CASCADE, related_name='employees')
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f"{self.user.username} - {self.school.name}"