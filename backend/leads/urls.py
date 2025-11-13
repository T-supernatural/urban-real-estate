from django.urls import path
from .views import LeadCreateView

urlpatterns = [
    path('', LeadCreateView.as_view(), name='lead-create'),
]
from django.urls import path
from .views import lead_create

urlpatterns = [
    path('', name='lead_create', view=lead_create),
]