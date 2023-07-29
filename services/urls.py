from django.urls import path, include
from . import views


urlpatterns = [
    path(
        "providers/",
        views.ProviderCreateAPIView.as_view(),
        name="list_create_providers",
    ),
    path(
        "providers/<int:pk>/",
        views.ProviderRetrieveAPIView.as_view(),
        name="get_update_delete_providers",
    ),
    path(
        "service-areas/",
        views.ServiceAreaCreateAPIView.as_view(),
        name="list_create_service_areas",
    ),
    path(
        "service-areas/<int:pk>/",
        views.ServiceAreaRetrieveAPIView.as_view(),
        name="get_update_delete_service_areas",
    ),
    path(
        "polygons/",
        views.PolygonAPIView.as_view(),
        name="get_polygons_list",
    ),
]
