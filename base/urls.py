# from django.contrib import admin
# from django.urls import path
# from customadmin.admin import custom_admin_site  # Import the custom admin site
# from . import views  # Import views for your app's homepage or other views
# from django.contrib.auth import views as auth_views
# # Define the URL patterns
# urlpatterns = [
#     path('admin/', admin.site.urls),  # Default Django admin site
#     path('customadmin/', custom_admin_site.urls), 
#     path('', views.home, name="home"),  # Your homepage or other app views
#     path('user/home/', views.user_home, name='user_home'),


#     path('adminportal/home/', views.admin_dashboard, name='admin_dashboard'),  
#     path('adminportal/employees/', views.admin_employees, name='admin_employees'),  
#     path('adminportal/departments/', views.admin_departments, name='admin_departments'),  
#     path('adminportal/sections/', views.admin_sections, name='admin_sections'),  
#     path('adminportal/sites/', views.admin_sites, name='admin_sites'),  
#     path('adminportal/leaveTypes/', views.admin_leaveTypes, name='admin_leaveTypes'),  
#     path('adminportal/reports/', views.admin_reports, name='admin_reports'),
#     path('adminportal/users/', views.admin_users, name='admin_users'),
#     path('adminportal/settings/', views.admin_settings, name='admin_settings'),
#    # Specify the custom login template
#     path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
# ]
from django.contrib import admin
from django.urls import path
from customadmin.admin import custom_admin_site  # Import the custom admin site
from base import views as base_views  # Import views for your app's homepage or other views from base
from customadmin import views as customadmin_views  # Import views for your APIs
from django.contrib.auth import views as auth_views

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Default Django admin site
    path('customadmin/', custom_admin_site.urls), 
    path('', base_views.home, name="home"),  # Your homepage or other app views
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
    path('api/sites/', customadmin_views.site_list, name='site-list'),  # Correctly import API views
    path('api/sites/<int:pk>/', customadmin_views.site_detail, name='site-detail'),

    # Specify the custom login template
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
