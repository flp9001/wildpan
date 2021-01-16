from django.contrib import admin

from .models import Follower
from .models import Profile

admin.site.register(Profile)
admin.site.register(Follower)
