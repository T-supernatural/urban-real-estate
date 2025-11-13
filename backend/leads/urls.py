from django.urls import path
from .views import lead_create

urlpatterns = [
    path('', name='lead_create', view=lead_create),
]