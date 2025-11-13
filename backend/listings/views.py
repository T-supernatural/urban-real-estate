from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def listing_list(request):
    return HttpResponse("This is the listing list view.")