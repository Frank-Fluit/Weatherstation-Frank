# dataprocessing/tests.py

from django.test import TestCase
# from rest_framework.test import APITestCase
# from rest_framework import status
from django.urls import reverse


class YourViewTests(TestCase):
    def test_url_for_view_hello(self):

        url = reverse('hello')
        self.assertEqual(url, '/dataprocessing/hello/')

    def test_url_for_view_csv(self):

        url = reverse('csv_processing')
        self.assertEqual(url, '/dataprocessing/csv/')

    def test_url_for_view_datapost(self):

        url = reverse('data_post')
        self.assertEqual(url, '/dataprocessing/datapost/')

    def test_url_for_view_compare(self):

        url = reverse('compare')
        self.assertEqual(url, '/dataprocessing/compare/')

    def test_url_for_view_correlation(self):

        url = reverse('correlation')
        self.assertEqual(url, '/dataprocessing/correlation/')
