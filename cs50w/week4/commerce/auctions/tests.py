from django.test import TestCase

# Create your tests here.
from .views import index, listing, create
from unittest import mock



def test_index()