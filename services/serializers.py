from rest_framework import serializers
from .models import Provider, ServiceArea


class ProviderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class ServiceAreaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = "__all__"


class PolygonSerializers(serializers.ModelSerializer):
    provider = serializers.SerializerMethodField()

    def get_provider(self, obj):
        return obj.provider.name

    class Meta:
        model = ServiceArea
        fields = ["name", "provider", "price"]
