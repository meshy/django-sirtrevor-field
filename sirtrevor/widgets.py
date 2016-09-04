from django.forms.widgets import Textarea


class SirTrevorWidget(Textarea):
    """Form widget for SirTrevorJS content."""
    class Media:
        css = {
            'all': ('sirtrevor/sir-trevor.min.css',),
        }
        js = (
            'sirtrevor/sir-trevor.min.js',
            'sirtrevor/sir-trevor-init.js',
        )

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}

        # Remove Textarea's row and cols default. They don't make sense given
        # the area's going to be blasted by SirTrevorJS.
        attrs.setdefault('cols', False)
        attrs.setdefault('rows', False)

        # Add a class for Sirtrevor JS to pick up on.
        attrs.setdefault('class', 'js-st-instance')
        super().__init__(attrs)
