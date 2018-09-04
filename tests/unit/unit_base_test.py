"""
UnitBaseTest

This class should be the parent class to each unit test.
This makes sure that any relevant classes are in the hierarchy for the
unit tests.
"""

from unittest import TestCase
from app import app


class UnitBaseTest(TestCase):
    pass