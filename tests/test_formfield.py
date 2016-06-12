from django.contrib.postgres.forms import JSONField
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.test import TestCase

from sirtrevor.formfields import SirTrevorField


class TestCleanEmptyValues(TestCase):
    """Ensure empty values are cleaned."""
    def test_required(self):
        """When required=True, an error is raised."""
        expected = 'This field is required'
        field = SirTrevorField(required=True)
        for value in EMPTY_VALUES:
            with self.subTest(empty_value=value):
                with self.assertRaisesMessage(ValidationError, expected):
                    field.clean(value)

    def test_unrequired(self):
        """When required=True, None is returned."""
        field = SirTrevorField(required=False)
        for value in EMPTY_VALUES:
            with self.subTest(empty_value=value):
                result = field.clean(value)
                self.assertEqual(result, None)


class TestSirTrevorField(TestCase):
    def test_is_field(self):
        """SirTrevorField is a subclass of JSONField."""
        self.assertTrue(issubclass(SirTrevorField, JSONField))
