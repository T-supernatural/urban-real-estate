from django.urls import path
from .views import LeadCreateView

urlpatterns = [
    # POST /api/v1/leads/ (Create a Lead)
    path('', LeadCreateView.as_view(), name='lead-create'),
]