from django import forms
from django.test import TestCase

from sirtrevor.formfields import SirTrevorField


class TestSirTrevorField(TestCase):
    def test_is_field(self):
        """SirTrevorField is a subclass of Field."""
        self.assertTrue(issubclass(SirTrevorField, forms.Field))
