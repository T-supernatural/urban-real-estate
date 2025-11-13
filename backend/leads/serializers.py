from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["id", "name", "email", "phone_number", "property_interested_in", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate(self, data):
        # Ensure at least one contact method is provided
        email = data.get("email")
        phone = data.get("phone_number")
        if not email and not phone:
            raise serializers.ValidationError("Provide at least an email or phone number.")
        return data