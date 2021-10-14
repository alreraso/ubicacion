import json
from django.http import response
from django.test.testcases import connections_support_transactions
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from direccion.models import Direccion

# Create your tests here.
class Direccion_test(TestCase):
    def setUp(self):
        return Direccion.objects.create(
            continente="North America",
            pais="United States",
            region="Oregon",
            ciudad="Portland",
            direccion="Calle falsa 123",
            latitud="41.23",
            longitud="122.35"
        )

    def test_all_ubicaciones(self):
        response = self.client.get("/direcciones/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_agregar_ubicacion(self):
        ubicacionpost={
            "continente":"North America",
            "pais":"United States",
            "region":"Oregon",
            "ciudad":"Portland",
            "direccion":"Calle falsa 123",
            "latitud":"41.23",
            "longitud":"122.35"
        }
        response = self.client.post("/direcciones/",ubicacionpost)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_put_ubicacion(self):
        response = self.client.put(reverse('putubicacion',kwargs={"pk":1}),{
            "continente":"North America",
            "pais":"United States",
            "region":"Oregon",
            "ciudad":"Portland",
            "direccion":"Calle verdaresa 345",
            "latitud":"23.23",
            "longitud":"72.35"
        },content_type='application/json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data["latitud"],"23.23")
        self.assertEqual(response.data["longitud"],"72.35")
        