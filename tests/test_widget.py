import json

from django.test import TestCase
from django.utils.html import format_html

from sirtrevor.widgets import SirTrevorWidget


class TestSirTrevorWidgetRender(TestCase):
    """Render tests for SirTrevorWidget."""
    def test_render_empty(self):
        """Just a basic textarea when empty."""
        result = SirTrevorWidget().render(name='test', value=None)
        expected = '<textarea class="js-st-instance" name="test">\r\n</textarea>'
        self.assertEqual(result, expected)

    def test_render_content(self):
        """When given json, it's rendered "escaped" in the page."""
        data = [{
            'type': 'video',
            'data': {'remote_id': 'dQw4w9WgXcQ', 'source': 'youtube'},
        }]
        json_content = json.dumps(data)
        result = SirTrevorWidget().render(name='test', value=json_content)
        template = '<textarea class="js-st-instance" name="test">\r\n{json}</textarea>'
        expected = format_html(template, json=json_content)
        self.assertEqual(result, expected)
