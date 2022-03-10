from rest_framework.serializers import Serializer

from .models import Calculation
from .tasks import supper_sum


class CalculationSerializer(Serializer):
    class Meta:
        model = Calculation
        fields = ["__all__"]
