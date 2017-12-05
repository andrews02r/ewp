from django.test import TestCase

# Create your tests here.

from .models import Stream, StreamType, StreamTokenType

class SteamTypeTestCase(TestCase):
    def setUp(self):
        Stream.objects.create(name="StreamType 1", description="StreamType 1 Description", active=True)
        Stream.objects.create(name="StreamType 2", description="StreamType 2 Description", active=False)

