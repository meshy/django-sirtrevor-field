"""Tests for the SirTrevorField model field."""
from django import forms
from django.contrib.postgres.fields import JSONField
from django.test import TestCase

from sirtrevor import formfields
from sirtrevor.modelfields import SirTrevorField


class TestFormField(TestCase):
    """Tests for SirTrevorField.formfield()."""
    def test_is_custom(self):
        """It returns our custom field by default."""
        expected = formfields.SirTrevorField
        returned = SirTrevorField().formfield()
        self.assertIsInstance(returned, expected)

    def test_is_dynamic(self):
        """It can be overridden.."""
        expected = forms.Field
        returned = SirTrevorField().formfield(form_class=expected)
        self.assertIsInstance(returned, expected)


class TestJSONField(TestCase):
    def test_is_jsonfield(self):
        """SirTrevorField is a subclass of JSONField."""
        self.assertTrue(issubclass(SirTrevorField, JSONField))
