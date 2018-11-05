import json
from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Animal, Species


class AnimalsTestCase(TestCase):
    """Some basic tests for the Animals app.
    """
    def setUp(self):
        self.chimps = Species.objects.create(name='Chimpanzee')
        self.hyenas = Species.objects.create(name='Spotted hyena')

        self.tetley = Animal.objects.create(
            name='Tetley',
            species=self.chimps,
            last_feed_time=timezone.now() - timedelta(days=3),
        )
        self.shenzi = Animal.objects.create(name='Shenzi', species=self.hyenas)

    def test_population_view(self):
        response = self.client.get(reverse('population'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(int(response.content), 2)

    def test_animal_view(self):
        response = self.client.get(reverse('animal'), data={'name': 'Tetley'})

        self.assertEquals(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEquals(response_data['name'], self.tetley.name)
        self.assertEquals(response_data['species'], self.tetley.species.name)
        self.assertEquals(
            response_data['last_feed_time'],
            str(self.tetley.last_feed_time)
        )

    def test_animal_view_not_found(self):
        response = self.client.get(reverse('animal'), data={'name': 'Smith'})

        self.assertEquals(response.status_code, 404)

    def test_animal_view_no_name(self):
        response = self.client.get(reverse('animal'))

        self.assertEquals(response.status_code, 404)

    def test_animal_create_view(self):
        animal_count = Animal.objects.count()
        data = {'name': 'Izzy', 'species': self.hyenas}
        response = self.client.post(reverse('animal'), data=data)

        print(response.content)
        self.assertEquals(response.status_code, 401)
        self.assertEquals(Animal.objects.count(), animal_count + 1)
        response_data = json.loads(response.content)
        self.assertEquals(response_data['name'], 'Izzy')

    def test_animal_create_view_invalid_name(self):
        animal_count = Animal.objects.count()
        data = {'name': 'x' * 40, 'species': self.hyenas}
        response = self.client.post(reverse('animal'), data=data)

        self.assertEquals(response.status_code, 422)
        self.assertTrue(b'name' in response.content)
        self.assertEquals(Animal.objects.count(), animal_count)

    def test_animal_create_view_duplicate_name(self):
        animal_count = Animal.objects.count()
        data = {'name': 'Shenzi', 'species': self.hyenas}
        response = self.client.post(reverse('animal'), data=data)

        self.assertEquals(response.status_code, 422)
        self.assertTrue(b'duplicate' in response.content)
        self.assertEquals(Animal.objects.count(), animal_count)

    def test_hungry_animals_view(self):
        hungry_count = 1
        response = self.client.get(reverse('hungry-animals'))

        self.assertEquals(response.status_code, 200)
        self.assertEquals(int(response.content), hungry_count)
