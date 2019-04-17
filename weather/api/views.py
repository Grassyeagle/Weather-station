from rest_framework import generics

from . import models , serializers

class TemperatureList(generics.ListCreateAPIView):
    queryset = models.Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer
    
class TemperatureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Temperature.objects.all()
    serializer_class = serializers.TemperatureSerializer

class HList(generics.ListCreateAPIView):
    queryset = models.Bp.objects.all()
    serializer_class = serializers.HSerializer
    
class HDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.H.objects.all()
    serializer_class = serializers.HSerializer
    
class BpList(generics.ListCreateAPIView):
    queryset = models.Bp.objects.all()
    serializer_class = serializers.BpSerializer
    
class BpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Bp.objects.all()
    serializer_class = serializers.BpSerializer