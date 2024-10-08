from rest_framework import serializers
from .models import Site, LeaveType ,Department, Section ,Employee

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
    department = serializers.SerializerMethodField()  # Use SerializerMethodField to avoid circular reference

    class Meta:
        model = Section
        fields = ['id', 'name', 'description', 'department']

    def get_department(self, obj):
        # Return department data manually
        department = obj.department
        return {
            'id': department.id,
            'name': department.name,
            'description': department.description,
        }
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
# class EmployeeSerializer(serializers.ModelSerializer):
#     # Use related serializers for site, department, and section
#     site = SiteSerializer(read_only=True)
#     department = DepartmentSerializer(read_only=True)
#     section = SectionSerializer(read_only=True)

#     # Expect the ID for writing operations
#     site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='site', write_only=True)
#     department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department', write_only=True)
#     section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), source='section', write_only=True)

#     class Meta:
#         model = Employee
#         fields = [
#             'employee_id', 'employee_name', 'phone', 'email',
#             'email_approver_l1', 'email_approver_l2', 'email_approver_l3',
#             'approver_email', 'aknowledge_by', 'site', 'department', 'section',
#             'site_id', 'department_id', 'section_id',  # These are for write operations
#             'status', 'allow_date'
#         ]
class EmployeeSerializer(serializers.ModelSerializer):
    site = SiteSerializer(read_only=True)
    section = SectionSerializer(read_only=True)

    site_id = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), source='site', write_only=True)
    section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), source='section', write_only=True)

    class Meta:
        model = Employee
        fields = [
            'employee_id', 'employee_name', 'phone', 'email',
            'email_approver_l1', 'email_approver_l2', 'email_approver_l3',
            'approver_email', 'aknowledge_by', 'site', 'site_id', 'section', 'section_id',
            'status', 'allow_date'
        ]

    def create(self, validated_data):
        # Get the section instance from the provided section_id
        section = validated_data.get('section')
        
        # Automatically set the department based on the selected section
        validated_data['department'] = section.department

        # Create the employee with the updated data
        return Employee.objects.create(**validated_data)