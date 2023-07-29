from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ServiceArea(models.Model):
    provider = models.ForeignKey(
        Provider, related_name="service_areas", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    geo_info = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
