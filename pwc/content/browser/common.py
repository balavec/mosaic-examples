from plone.app.layout.globals.interfaces import IBodyClassAdapter
from zope.interface import implementer


@implementer(IBodyClassAdapter)
class CustomBodyClass(object):
    """Add custom body class based on layout name
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_classes(self, template, view):
        """Body classes adapter.
        """
        layout = getattr(self.context, 'layout', None)
        if layout == 'fullwidth_layout_view':
            return ['fullwidth_mosaic_layout']
        return []


NEW_LAYOUT_VIEWS = [
    'layout_view', '@@layout_view',
    'fullwidth_layout_view', '@@fullwidth_layout_view',
    ]


def patched_layout_view():
    return NEW_LAYOUT_VIEWS


def apply_patched_layout(scope, original, replacement):
    setattr(scope, original, replacement())
    return
