#Source: https://stackoverflow.com/questions/57537309/typeerror-str-returned-non-string-type-magicmock
import factory
import mock
from imagekit.signals import source_saved
from .mocks import storage_mock, image_mock
from .models import Car


@factory.django.mute_signals(source_saved)
class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    image = image_mock


def test_case_one(self):
    with mock.patch('django.core.files.storage.default_storage._wrapped', storage_mock):
        car = CarFactory.create()