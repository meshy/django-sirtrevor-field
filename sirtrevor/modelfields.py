from django.contrib.postgres.fields import JSONField

from . import formfields


class SirTrevorField(JSONField):
    """Modelfield for SirTrevor json content."""
    def formfield(self, **kwargs):
        """Override default form field."""
        kwargs.setdefault('form_class', formfields.SirTrevorField)
        return super().formfield(**kwargs)
