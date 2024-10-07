from rest_framework import serializers
from .models import Site, LeaveType  # Make sure to import LeaveType

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'location', 'description', 'status']

class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType  # Reference the LeaveType model here
        fields = ['id', 'name_kh', 'name_en', 'description', 'status']
