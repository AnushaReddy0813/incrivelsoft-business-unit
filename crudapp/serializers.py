from rest_framework import serializers
from .models import TimeStampModel,Business
class TimeStampModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=TimeStampModel
        fields='__all__'
class BusinessSerializer(TimeStampModelSerializer):
    class Meta:
        model=Business
        fields='__all__'             