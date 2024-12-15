from rest_framework import serializers
from .models import AirQualityIndex

class AirQualityIndexSerializers(serializers.ModelSerializer):
    class Meta:
        models=AirQualityIndex
        fields ='__all__'
