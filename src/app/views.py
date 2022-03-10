from rest_framework.generics import ListCreateAPIView
from models import Calculation
from serializers import CalculationSerializer



class CalculationApiView(ListCreateAPIView):
    model=Calculation
    serializer=CalculationSerializer
