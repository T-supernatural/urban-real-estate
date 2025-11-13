from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone_number", "property_interested_in", "created_at")
	list_filter = ("created_at", "property_interested_in")
	search_fields = ("name", "email", "phone_number")
	readonly_fields = ("created_at",)
