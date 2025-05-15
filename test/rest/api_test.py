import http.client
import os
import unittest
import json
from urllib.request import urlopen

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
        content = response.read().decode('utf-8')
        self.assertEqual(content, "4")

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertEqual(content, "2")

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertEqual(content, "6")

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/6/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertEqual(content, "3.0")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/6/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP, pero no se recibió")
        except Exception as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            content = e.read().decode('utf-8')
            self.assertIn("Division by zero is not possible", content)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertEqual(content, "8.0")

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertEqual(content, "3.0")

    def test_api_sqrt_negative(self):
        url = f"{BASE_URL}/calc/sqrt/-1"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP, pero no se recibió")
        except Exception as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            content = e.read().decode('utf-8')
            self.assertIn("Cannot calculate square root of negative number", content)

    def test_api_log10(self):
        url = f"{BASE_URL}/calc/log10/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        content = response.read().decode('utf-8')
        self.assertEqual(content, "2.0")

    def test_api_log10_negative_or_zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
            self.fail("Se esperaba un error HTTP, pero no se recibió")
        except Exception as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            content = e.read().decode('utf-8')
            self.assertIn("Cannot calculate logarithm of zero or negative number", content)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()