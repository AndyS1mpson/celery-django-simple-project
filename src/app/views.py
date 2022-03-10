from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Calculation
from .serializers import CalculationSerializer
from .tasks import supper_sum


class CalculationApiView(ListCreateAPIView):
    model=Calculation

    def create(self, request, x: int, y: int):
        name = request.data["name"]
        res = supper_sum.delay(x, y).get()
        Calculation.objects.create(
            name=name,
            value=res
        )
        return Response(
            status=201
        )
