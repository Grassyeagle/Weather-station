from rest_framework import serializers
from . import models


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'celsius', 'change', 'change', 'record_time',)
        model = models.Temperature