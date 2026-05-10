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