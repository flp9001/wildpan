from .base import *  # noqa
from .base import env  # noqa

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda r: env.str(
        "DJANGO_DEBUG_TOOLBAR", True
    ),  # disables it
    # '...
}


INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
