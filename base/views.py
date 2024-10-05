from django.shortcuts import render
from . import views
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'index.html')
def user_home(request):
    return render(request, 'User/Home.html')
@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')
@login_required
def admin_employees(request):
    return render(request, 'admin/employees.html')
@login_required
def admin_departments(request):
    return render(request, 'admin/departments.html')
@login_required
def admin_sections(request):
    return render(request, 'admin/sections.html')
@login_required
def admin_sites(request):
    return render(request, 'admin/sites.html')
@login_required
def admin_leaveTypes(request):
    return render(request, 'admin/leaveTypes.html')
@login_required
def admin_reports(request):
    return render(request, 'admin/reports.html')
@login_required
def admin_users(request):
    return render(request, 'admin/users.html')
@login_required
def admin_settings(request):
    return render(request, 'admin/settings.html')
