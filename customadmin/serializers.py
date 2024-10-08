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
class SectionSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to handle department for POST/PUT requests
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department')

    # Still return full department data when reading (GET requests)
    department = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ['id', 'name', 'description', 'department', 'department_id']  # department_id for POST, department for GET

    def get_department(self, obj):
        # Manually return department data without nesting
        department = obj.department
        return {
            'id': department.id,
            'name': department.name,
            'description': department.description,
        }

# DepartmentSerializer to show department and its related sections
class DepartmentSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()  # Nested SectionSerializer to show related sections

    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'sections']  # Include sections field

    def get_sections(self, obj):
        # Use the related_name 'sections' for reverse lookup
        sections = obj.sections.all()  # 'sections' is the related_name in the ForeignKey
        return SectionSerializer(sections, many=True, read_only=True).data

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