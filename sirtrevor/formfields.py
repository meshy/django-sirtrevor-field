from django.contrib.postgres.forms import JSONField

from sirtrevor.widgets import SirTrevorWidget


class SirTrevorField(JSONField):
    """Formfield for SirTrevor json content."""
    widget = SirTrevorWidget

    def __init__(self, **kwargs):
        """
        Override the default widget.

        Required until https://github.com/django/django/pull/6764 released.
        """
        kwargs.setdefault('widget', self.widget)
        super().__init__(**kwargs)
