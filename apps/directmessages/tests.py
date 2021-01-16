from django.test import TestCase
from django.utils import timezone

from .models import Message
from apps.users.models import User


class MessageTestCase(TestCase):
    def create_message(
        self,
        sender=User.objects.get(id=1),
        receiver=User.objects.get(id=2),
        content="test message",
    ):
        return Message.objects.create(
            sender=sender,
            receiver=receiver,
            content=content,
            date_created=timezone.now(),
        )

    def test_message_creation(self):
        message = self.create_message()
        self.assertTrue(isinstance(message, Message))
        self.assertEqual(message.__str__(), message.content)
