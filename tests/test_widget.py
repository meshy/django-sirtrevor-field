from django.test import TestCase

from sirtrevor.widgets import SirTrevorWidget


class TestSirTrevorWidgetRender(TestCase):
    """Render tests for SirTrevorWidget."""
    def test_render_empty(self):
        """Just a basic textarea when empty."""
        result = SirTrevorWidget().render(name='test', value=None)
        expected = '<textarea name="test">\r\n</textarea>'
        self.assertEqual(result, expected)
