from django.db import models

from django.core.validators import MinValueValidator

class TimeEntry(models.Model):
    project_name=models.CharField(max_length=100)
    description=models.TextField()
    hours=models.FloatField(validators=[MinValueValidator(0.1)])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Time entry"

    def __str__(self):
        return f"{self.project_name} - {self.hours}h"
