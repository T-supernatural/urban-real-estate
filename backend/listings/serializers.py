from rest_framework import serializers
from .models import Listing, ListingImage


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ["id", "image", "caption", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


class ListingSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = [
            "id",
            "title",
            "description",
            "price",
            "location",
            "bedrooms",
            "bathrooms",
            "size_sqft",
            "is_published",
            "photos",
            "images",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "images"]
