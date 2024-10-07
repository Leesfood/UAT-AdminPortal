# customadmin/views.py

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from .models import Site
# from .serializers import SiteSerializer
from .models import Site, LeaveType
from .serializers import SiteSerializer, LeaveTypeSerializer
from django.http import JsonResponse
# Existing views
def home(request):
    return render(request, 'home.html')

# List all sites or create a new site
@api_view(['GET', 'POST'])
def site_list(request):
    # GET: List all sites
    if request.method == 'GET':
        sites = Site.objects.all()
        serializer = SiteSerializer(sites, many=True)
        return Response(serializer.data)

    # POST: Create a new site
    elif request.method == 'POST':
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific site
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def site_detail(request, pk):
    site = get_object_or_404(Site, pk=pk)

    # GET: Retrieve a single site
    if request.method == 'GET':
        serializer = SiteSerializer(site)
        return Response(serializer.data)

    # PUT: Update an entire site
    elif request.method == 'PUT':
        serializer = SiteSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH: Partially update a site
    elif request.method == 'PATCH':
        serializer = SiteSerializer(site, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete a site
    elif request.method == 'DELETE':
        site.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Add this function to avoid the error
def user_home(request):
    return render(request, 'user/home.html')

# List all leave types or create a new leave type
@api_view(['GET', 'POST'])
def leave_type_list(request):
    if request.method == 'GET':
        leave_types = LeaveType.objects.all()
        serializer = LeaveTypeSerializer(leave_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LeaveTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Retrieve, update, or delete a specific leave type
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def leave_type_detail(request, pk):
    leave_type = get_object_or_404(LeaveType, pk=pk)

    if request.method == 'GET':
        serializer = LeaveTypeSerializer(leave_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LeaveTypeSerializer(leave_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = LeaveTypeSerializer(leave_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        leave_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)