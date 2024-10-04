from django.contrib import admin
from django.urls import path
from customadmin.admin import custom_admin_site  # Import the custom admin site
from . import views  # Import views for your app's homepage or other views
from django.contrib.auth import views as auth_views
# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Default Django admin site
    path('customadmin/', custom_admin_site.urls), 
    path('', views.home, name="home"),  # Your homepage or other app views
    path('adminportal/home/', views.admin_dashboard, name='admin_dashboard'),  
    path('adminportal/employees/', views.admin_employees, name='admin_employees'),  
    path('adminportal/departments/', views.admin_departments, name='admin_departments'),  
    path('adminportal/sections/', views.admin_sections, name='admin_sections'),  
    path('adminportal/sites/', views.admin_sites, name='admin_sites'),  
    path('adminportal/reports/', views.admin_reports, name='admin_reports'),
    path('adminportal/users/', views.admin_users, name='admin_users'),
    path('adminportal/settings/', views.admin_settings, name='admin_settings'),
   # Specify the custom login template
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
