from rest_framework.serializers import Serializer
from models import Calculation
from .tasks import supper_sum


class CalculationSerializer(Serializer):
    model=Calculation
    
    def create(self, validated_data):
        supper_sum.delay(5, 7)
        return super()
