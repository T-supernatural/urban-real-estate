from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lead_create(request):
    return HttpResponse("This is the lead page.")