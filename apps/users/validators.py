import re

from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.]+$"
    message = _(
        "Enter a valid username. This value may contain only English letters, "
        "numbers, and . _ characters."
    )
    flags = re.ASCII


@deconstructible
class ReservedValidator(object):
    code = "invalid"
    message = _("You cant use {} as a username.")

    RESERVED = {
        "__debug__",
        "about",
        "admin",
        "comment",
        "explore",
        "followuser",
        "inbox",
        "likepost",
        "login",
        "logout",
        "media",
        "messages",
        "password-reset",
        "password-reset-complete",
        "password-reset-confirm",
        "post",
        "profile",
        "register",
        "search",
    }

    def __call__(self, value):
        """
        Validate that the input contains (or does *not* contain, if
        inverse_match is True) a match for the regular expression.
        """
        if str(value).lower() in self.RESERVED:
            raise ValidationError(self.message.format(value), code=self.code)
