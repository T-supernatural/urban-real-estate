from django.contrib import admin
from .models import Listing, ListingImage


class ListingImageInline(admin.TabularInline):
	model = ListingImage
	extra = 1


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
	list_display = (
		"title",
		"price",
		"location",
		"bedrooms",
		"bathrooms",
		"is_published",
		"created_at",
	)
	list_filter = ("is_published", "created_at")
	search_fields = ("title", "description", "location")
	inlines = (ListingImageInline,)


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
	list_display = ("listing", "caption", "uploaded_at")
	search_fields = ("caption",)
admin