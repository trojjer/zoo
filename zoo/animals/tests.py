from django.test import TestCase
from django.urls import reverse

from .models import Animal, Species


class AnimalsTestCase(TestCase):
    """Some basic tests for the Animals app.
    """
    def setUp(self):
        chimps = Species.objects.create(name='Chimpanzee')
        hyenas = Species.objects.create(name='Spotted hyena')

        Animal.objects.create(name='Tetley', species=chimps)
        Animal.objects.create(name='Shenzi', species=hyenas)

    def test_population_view(self):
        response = self.client.get(reverse('population'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, b'2')
