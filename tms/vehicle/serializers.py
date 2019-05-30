from rest_framework import serializers

from . import models as m
from ..job.models import Job


class ShortVehicleSerializer(serializers.ModelSerializer):
    """
    Serializer for short data of vehicle
    """
    class Meta:
        model = m.Vehicle
        fields = (
            'id', 'plate_num'
        )


class MainVehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Vehicle
        fields = (
            'id', 'plate_num', 'longitude', 'latitude', 'speed'
        )


class VehicleSerializer(serializers.ModelSerializer):
    """
    Vehicle serializer
    """
    model_name = serializers.CharField(
        source='get_model_display', read_only=True
    )
    brand_name = serializers.CharField(
        source='get_brand_display',
        read_only=True
    )
    jobs = serializers.SerializerMethodField()

    class Meta:
        model = m.Vehicle
        fields = (
            'id', 'model', 'model_name', 'plate_num', 'code', 'brand',
            'brand_name', 'load', 'longitude', 'latitude', 'jobs'
        )

    def get_jobs(self, obj):
        return obj.jobs.count()


class VehicleDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.VehicleDocument
        fields = '__all__'


class VehiclePositionSerializer(serializers.ModelSerializer):
    """
    Serializer for vehicle playback
    """
    lnglat = serializers.SerializerMethodField()

    class Meta:
        model = m.Vehicle
        fields = (
            'id', 'speed', 'lnglat'
        )

    def get_lnglat(self, obj):
        return [obj.longitude, obj.latitude]
