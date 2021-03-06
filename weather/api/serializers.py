from rest_framework import serializers
from . import models


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'celsius', 'change', 'record_time',)
        model = models.Temperature
        
class HSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'rh', 'change', 'record_time',)
        model = models.H
        
class BpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'p', 'change', 'record_time',)
        model = models.Bp