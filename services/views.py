from django.db.models import Q
from rest_framework import generics, views, permissions, status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Provider, ServiceArea
from .serializers import ProviderSerializers, ServiceAreaSerializers, PolygonSerializers


class ProviderCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProviderSerializers
    queryset = Provider.objects.all()


class ProviderRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProviderSerializers
    queryset = Provider.objects.all()


class ServiceAreaCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiceAreaSerializers
    queryset = ServiceArea.objects.all()


class ServiceAreaRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ServiceAreaSerializers
    queryset = ServiceArea.objects.all()


class PolygonAPIView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PolygonSerializers

    def get_queryset(self):
        lat = eval(self.request.query_params.get("lat"))
        lng = eval(self.request.query_params.get("lng"))
        return ServiceArea.objects.filter(
            Q(geo_info__coordinates__0__contains=[[lat, lng]])
            | Q(geo_info__coordinates__0__contains=[lat, lng])
        )

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "lat", openapi.IN_QUERY, description="lat", type=openapi.TYPE_NUMBER
            ),
            openapi.Parameter(
                "lng", openapi.IN_QUERY, description="lng", type=openapi.TYPE_NUMBER
            ),
        ],
        responses={200: PolygonSerializers},
    )
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
