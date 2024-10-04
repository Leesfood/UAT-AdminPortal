from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from django.contrib.admin import AdminSite

# Create the custom AdminSite
class CustomAdminSite(AdminSite):
    site_header = "Custom Admin Dashboard"
    site_title = "Custom Admin Portal"
    index_title = "Welcome to the Custom Admin Dashboard"

    # Override the index view to add extra context
    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['total_users'] = User.objects.count()  # Add total users count
        extra_context['total_groups'] = Group.objects.count()  # Add total groups count
        return super().index(request, extra_context=extra_context)

# Instantiate the custom admin site **before** registering models
custom_admin_site = CustomAdminSite(name='customadmin')

# Unregister default User and Group from the default admin site
admin.site.unregister(User)
admin.site.unregister(Group)

# Register User and Group models to the custom admin site
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class CustomGroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
