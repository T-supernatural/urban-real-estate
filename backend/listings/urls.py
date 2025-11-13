from django.urls import path
from .views import listing_list

urlpatterns = [
    path('', name='listing_list', view=listing_list),
]