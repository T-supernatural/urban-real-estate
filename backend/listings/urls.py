from django.urls import path
from .views import ListingListView, ListingDetailView

urlpatterns = [
    path('', ListingListView.as_view(), name='listing-list'),
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
]