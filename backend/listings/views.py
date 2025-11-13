from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing
from .serializers import ListingSerializer


class ListingListView(generics.ListAPIView):
    """List all published listings with filtering and search."""

    queryset = Listing.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {"price": ["gte", "lte"], "bedrooms": ["exact"], "location": ["icontains"]}
    search_fields = ["title", "description", "location"]
    ordering_fields = ["price", "created_at", "bedrooms"]
    ordering = ["-created_at"]
    pagination_class = None  # Optional: add pagination later


class ListingDetailView(generics.RetrieveAPIView):
    """Retrieve a single listing with all details and images."""

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = "pk"