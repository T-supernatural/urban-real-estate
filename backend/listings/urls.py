from django.urls import path
from .views import ListingListView, ListingDetailView

urlpatterns = [
    # GET /api/v1/listings/ (List and Search)
    path('', ListingListView.as_view(), name='listing-list'),
    
    # GET /api/v1/listings/123/ (Retrieve Detail)
    path('<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
]