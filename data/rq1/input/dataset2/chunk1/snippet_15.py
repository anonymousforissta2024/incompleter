#Source: https://stackoverflow.com/questions/29653129/update-to-django-1-8-attributeerror-django-test-testcase-has-no-attribute-cl
import django
import unittest
from django.test import TestCase
import logging
import sys
from builtins import classmethod, isinstance

class ATestTests(TestCase):

    @classmethod
    def setUpClass(cls):
        django.setup()
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


    def setUp(self):
        self._app = Application(name="a")


    def testtest(self):

        self.assertIsNotNone(self._app)