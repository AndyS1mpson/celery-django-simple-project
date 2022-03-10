from django.urls import path
from .views import CalculationApiView


urlpatterns = [
    path('calculate/<int:x>/<int:y>', CalculationApiView.as_view())
]
