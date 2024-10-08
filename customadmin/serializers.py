from rest_framework import serializers
from .models import Site, LeaveType ,Department, Section 

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'location', 'description', 'status']

class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType  # Reference the LeaveType model here
        fields = ['id', 'name_kh', 'name_en', 'description', 'status']

# Define DepartmentSerializer first
class DepartmentSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()  # Nested SectionSerializer to show related sections

    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'sections']  # Include sections field

    # Custom method to get related sections
    def get_sections(self, obj):
        sections = obj.sections.all()  # Assuming 'sections' is the related name in the Section model
        return SectionSerializer(sections, many=True, read_only=True).data


# Now define SectionSerializer after DepartmentSerializer
class SectionSerializer(serializers.ModelSerializer):
    # Only include department ID to avoid circular references
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department')

    class Meta:
        model = Section
        fields = ['id', 'name', 'description', 'department_id']  # Include department_id for write operations

# For POST Department
# {
#     "name": "IT",
#     "description": "Information Technology Department"
# }

# for POST SECTION
# {
#     "name": "Developer",
#     "description": "Handles development tasks",
#     "department": 1
# }
