from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from imagefield.fields import ImageField
from notifications.signals import notify

from .fields import LowercaseCharField
from .validators import ReservedValidator
from .validators import UsernameValidator


class User(AbstractUser):
    """Default user for My Awesome Project.
    """

    username = LowercaseCharField(
        _("username"),
        max_length=30,
        unique=True,
        help_text=_(
            "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[UsernameValidator(), ReservedValidator()],
        error_messages={"unique": _("A user with that username already exists.")},
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ImageField(
        default="default.jpg", upload_to="profile_pics", auto_add_fields=True
    )
    bio = models.CharField(max_length=150, blank=True)
    # bio is a field in this Post model. it specifies a class attribute Charfield and represents a database column
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class Follower(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="followers"
    )
    being_followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="being_followeds"
    )
    date_followed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.follower.username, self.being_followed.username} follower-> followee"

    def save(self, *args, **kwargs):
        super(Follower, self).save(*args, **kwargs)
        notify.send(
            self.follower,
            recipient=self.being_followed,
            verb="followed you!",
            description="follow",
            target=self,
        )
