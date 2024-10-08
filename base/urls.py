
from django.contrib import admin
from django.urls import path
from customadmin.admin import custom_admin_site 
from base import views as base_views 
from customadmin import views as customadmin_views 
from django.contrib.auth import views as auth_views

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('customadmin/', custom_admin_site.urls), 
    path('', base_views.home, name="home"),
    path('user/home/', base_views.user_home, name='user_home'),

    # Admin portal routes
    path('adminportal/home/', base_views.admin_dashboard, name='admin_dashboard'),  
    path('adminportal/employees/', base_views.admin_employees, name='admin_employees'),  
    path('adminportal/departments/', base_views.admin_departments, name='admin_departments'),  
    path('adminportal/sections/', base_views.admin_sections, name='admin_sections'),  
    path('adminportal/sites/', base_views.admin_sites, name='admin_sites'),  
    path('adminportal/leaveTypes/', base_views.admin_leaveTypes, name='admin_leaveTypes'),  
    path('adminportal/reports/', base_views.admin_reports, name='admin_reports'),
    path('adminportal/users/', base_views.admin_users, name='admin_users'),
    path('adminportal/settings/', base_views.admin_settings, name='admin_settings'),

    # API routes for customadmin
    path('api/sites/', customadmin_views.site_list, name='site-list'), 
    path('api/sites/<int:pk>/', customadmin_views.site_detail, name='site-detail'),
    path('api/leavetypes/',  customadmin_views.leave_type_list, name='leave_type_list'),
    path('api/leavetypes/<int:pk>/', customadmin_views.leave_type_detail, name='leave_type_detail'),
    path('api/departments/', customadmin_views.department_list, name='department-list'),
    path('api/departments/<int:pk>/', customadmin_views.department_detail, name='department-detail'),
    path('api/sections/', customadmin_views.section_list, name='section-list'),
    path('api/sections/<int:pk>/', customadmin_views.section_detail, name='section-detail'),
  # Corrected version:
    path('api/employees/', customadmin_views.employee_list, name='employee-list'),
    path('api/employees/<int:pk>/', customadmin_views.employee_detail, name='employee-detail'),

    # Specify the custom login template
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
