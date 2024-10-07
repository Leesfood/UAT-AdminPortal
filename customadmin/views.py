# customadmin/views.py

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Site
from .serializers import SiteSerializer
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
