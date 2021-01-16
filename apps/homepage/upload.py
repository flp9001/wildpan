import random
import string
from os.path import join
from os.path import normpath
from os.path import splitext

from django.utils import timezone
from django.utils.deconstruct import deconstructible

alpha = string.ascii_lowercase + string.digits


MAX_LEN_FILENAME = 12


@deconstructible
class UploadToPath(object):
    def __init__(self, upload_to):
        self.upload_to = upload_to

    def __call__(self, instance, filename):
        instance.original_file_name = filename
        return self.get_path(instance, filename)

    def _generate_directory_name(self, instance, filename):
        now = timezone.now()
        date = str(now.date()).replace("-", "/")
        base_folder = instance.post.author.username
        return normpath(join(self.upload_to, base_folder, date))

    def _generate_filename(self, filename):
        name, ext = splitext(filename)
        ext = ext.lower()
        new_filename = "".join(
            [random.SystemRandom().choice(alpha) for i in range(MAX_LEN_FILENAME)]
        )
        new_name = f"{new_filename}{ext}"

        return new_name

    def get_path(self, instance, filename):
        return join(
            self._generate_directory_name(instance, filename),
            self._generate_filename(filename),
        )
