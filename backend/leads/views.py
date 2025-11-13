from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LeadSerializer


class LeadCreateView(APIView):
    """POST-only endpoint to capture leads from the frontend."""

    def post(self, request, format=None):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lead_create(request):
    return HttpResponse("This is the lead page.")