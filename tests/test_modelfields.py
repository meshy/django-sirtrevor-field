"""Tests for the SirTrevorField model field."""
from django.contrib.postgres.fields import JSONField
from django.test import TestCase

from sirtrevor.modelfields import SirTrevorField


class TestJSONField(TestCase):
    def test_is_jsonfield(self):
        """SirTrevorField is a subclass of JSONField."""
        self.assertTrue(issubclass(SirTrevorField, JSONField))
