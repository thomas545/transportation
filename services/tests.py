from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Provider, ServiceArea


class ProviderTests(APITestCase):
    def test_create_provider(self):
        """
        Ensure we can create a new Provider object.
        """
        url = reverse("list_create_providers")
        data = {
            "name": "thomas",
            "email": "thomas@mozio.com",
            "phone_number": "01030346243",
            "language": "en",
            "currency": "USD",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, "thomas")

    def test_get_list_provider(self):
        """
        Ensure we can create a new Provider object.
        """
        Provider.objects.create(
            **{
                "name": "thomas",
                "email": "thomas@mozio.com",
                "phone_number": "01030346243",
                "language": "en",
                "currency": "USD",
            }
        )
        url = reverse("list_create_providers")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Provider.objects.count(), len(response.json().get("results")))

    def test_get_empty_list_provider(self):
        """
        Ensure we can create a new Provider object.
        """
        url = reverse("list_create_providers")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Provider.objects.count(), len(response.json().get("results")))

    def test_get_provider_by_id(self):
        """
        Ensure we can create a new Provider object.
        """
        obj = Provider.objects.create(
            **{
                "name": "thomas",
                "email": "thomas@mozio.com",
                "phone_number": "01030346243",
                "language": "en",
                "currency": "USD",
            }
        )
        url = reverse("get_update_delete_providers", kwargs={"pk": obj.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(obj.name, response.json().get("name"))
        self.assertEqual(obj.pk, response.json().get("id"))

    def test_update_provider_by_id(self):
        """
        Ensure we can create a new Provider object.
        """
        obj = Provider.objects.create(
            **{
                "name": "thomas",
                "email": "thomas@mozio.com",
                "phone_number": "01030346243",
                "language": "en",
                "currency": "USD",
            }
        )
        url = reverse("get_update_delete_providers", kwargs={"pk": obj.pk})
        response = self.client.patch(url, data={"name": "Saied"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(obj.name, "Saied")
        self.assertEqual(obj.pk, response.json().get("id"))

    def test_delete_provider_by_id(self):
        """
        Ensure we can create a new Provider object.
        """
        obj = Provider.objects.create(
            **{
                "name": "thomas",
                "email": "thomas@mozio.com",
                "phone_number": "01030346243",
                "language": "en",
                "currency": "USD",
            }
        )
        url = reverse("get_update_delete_providers", kwargs={"pk": obj.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ServiceAreaTests(APITestCase):
    @property
    def create_provider(self):
        provider = Provider.objects.create(
            **{
                "name": "thomas",
                "email": "thomas@mozio.com",
                "phone_number": "01030346243",
                "language": "en",
                "currency": "USD",
            }
        )
        return provider

    def create_service_area_obj(self):
        obj = ServiceArea.objects.create(
            **{
                "name": "service-0",
                "price": 300,
                "geo_info": {
                    "type": "Polygon",
                    "coordinates": [
                        [50, 40],
                        [20, 60],
                        [20, 40],
                        [50.9, 80.9],
                        [30.2, 40.8],
                    ],
                },
                "provider": self.create_provider,
            }
        )
        return obj

    def test_create_service_area(self):
        """
        Ensure we can create a new ServiceArea object.
        """
        url = reverse("list_create_service_areas")
        data = {
            "name": "service-0",
            "price": 300,
            "geo_info": {
                "type": "Polygon",
                "coordinates": [
                    [50, 40],
                    [20, 60],
                    [20, 40],
                    [50.9, 80.9],
                    [30.2, 40.8],
                ],
            },
            "provider": self.create_provider.pk,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().name, "service-0")

    def test_get_list_service_area(self):
        """
        Ensure we can create a new Provider object.
        """
        self.create_service_area_obj()

        url = reverse("list_create_service_areas")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            ServiceArea.objects.count(), len(response.json().get("results"))
        )

    def test_get_empty_list_service_area(self):
        """
        Ensure we can create a new Provider object.
        """
        url = reverse("list_create_service_areas")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            ServiceArea.objects.count(), len(response.json().get("results"))
        )

    def test_get_service_area_by_id(self):
        """
        Ensure we can create a new Provider object.
        """

        obj = self.create_service_area_obj()
        url = reverse("get_update_delete_service_areas", kwargs={"pk": obj.pk})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(obj.name, response.json().get("name"))
        self.assertEqual(obj.pk, response.json().get("id"))

    def test_update_service_area_by_id(self):
        """
        Ensure we can create a new Provider object.
        """

        obj = self.create_service_area_obj()
        url = reverse("get_update_delete_service_areas", kwargs={"pk": obj.pk})
        response = self.client.patch(url, data={"name": "service-001"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(obj.name, "service-001")
        self.assertEqual(obj.pk, response.json().get("id"))

    def test_delete_service_area_by_id(self):
        """
        Ensure we can create a new Provider object.
        """
        obj = self.create_service_area_obj()
        url = reverse("get_update_delete_service_areas", kwargs={"pk": obj.pk})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PolygonTests(APITestCase):
    @property
    def create_provider(self):
        provider = Provider.objects.create(
            **{
                "name": "thomas",
                "email": "thomas@mozio.com",
                "phone_number": "01030346243",
                "language": "en",
                "currency": "USD",
            }
        )
        return provider

    def create_service_area_obj(self):
        obj = ServiceArea.objects.create(
            **{
                "name": "service-0",
                "price": 300,
                "geo_info": {
                    "type": "Polygon",
                    "coordinates": [
                        [50, 40],
                        [20, 60],
                        [20, 40],
                        [50.9, 80.9],
                        [30.2, 40.8],
                    ],
                },
                "provider": self.create_provider,
            }
        )
        return obj

    def test_polygons_list(self):
        """
        Ensure we can create a new ServiceArea object.
        """
        self.create_service_area_obj()
        self.create_service_area_obj()
        self.create_service_area_obj()
        url = reverse("get_polygons_list")
        url = f"{url}?lat=50&lng=40"
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get("results")), 3)
