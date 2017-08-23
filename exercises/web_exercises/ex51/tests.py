# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.urls import reverse


class FormTests(TestCase):

    def test_get(self):
        response = self.client.get(reverse('ex51:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Exercise 51')
        self.assertEqual(response.context['name'], 'Nobody')

    def test_post(self):
        url = reverse('ex51:index')
        params =  {'hello': 'Hola', 'name': 'Radda'}
        response = self.client.post(url, params)
        self.assertContains(response, 'Radda')
        self.assertContains(response, 'Hola')

    def test_error_message(self):
        url = reverse('ex51:index')
        params =  {'hello': 'Hola'}
        response = self.client.post(url, params)
        self.assertContains(response, 'Hello and name are required')
