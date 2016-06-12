from django.forms.widgets import Textarea


class SirTrevorWidget(Textarea):
    """Form widget for SirTrevorJS content."""
    def __init__(self, attrs=None):
        """
        Remove Textarea's row and cols default.

        They don't make sense given the area's going to be blasted by
        SirTrevorJS.
        """
        if attrs is None:
            attrs = {}
        attrs.setdefault('cols', False)
        attrs.setdefault('rows', False)
        super().__init__(attrs)
