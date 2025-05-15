import http.client
import os
import unittest
from urllib.request import urlopen
import urllib.error

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode('utf-8'), "4", "Resultado incorrecto"
        )

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode('utf-8'), "2", "Resultado incorrecto"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode('utf-8'), "12", "Resultado incorrecto"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode('utf-8'), "5.0", "Resultado incorrecto"
        )

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode('utf-8'), "8", "Resultado incorrecto"
        )

    def test_api_square_root(self):
        url = f"{BASE_URL}/calc/square_root/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode('utf-8'), "3.0", "Resultado incorrecto"
        )

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode('utf-8'), "2.0", "Resultado incorrecto"
        )
        
    def test_api_invalid_params(self):
        url = f"{BASE_URL}/calc/add/2/abc"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba error 400")
        except urllib.error.HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error incorrecto en la petición API a {url}"
            )
            
    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba error 400")
        except urllib.error.HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error incorrecto en la petición API a {url}"
            )
            
    def test_api_negative_square_root(self):
        url = f"{BASE_URL}/calc/square_root/-1"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba error 400")
        except urllib.error.HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error incorrecto en la petición API a {url}"
            )
            
    def test_api_nonpositive_log10(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba error 400")
        except urllib.error.HTTPError as e:
            self.assertEqual(
                e.code, http.client.BAD_REQUEST, f"Error incorrecto en la petición API a {url}"
            )