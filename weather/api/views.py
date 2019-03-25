from rest_framework import generics

from .models import Temperature
from .serializers import TemperatureSerializer
# Create your views here.
class TemperatureList(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer


class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer