from rest_framework import serializers

from .models import TimeEntry

class TimeEntrySerializer(serializers.ModedlSerializer):
    class Meta:
        model=TimeEntry
        fields='__all__'
