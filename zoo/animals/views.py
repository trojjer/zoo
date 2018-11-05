from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Animal


class AnimalPopulationView(View):
    """Show a count of the current zoo population.
    """
    model = Animal

    def get(self, *args, **kwargs):
        return HttpResponse(self.model.objects.count())


class AnimalView(View):
    """GET an Animal by name, or create one with POST.
    """
    model = Animal

    def get(self, request, *args, **kwargs):
        animal_name = request.GET.get('name')
        animal = get_object_or_404(self.model, name=animal_name)
        animal_keys = ['name', 'species', 'last_feed_time']
        animal_data = {k: str(getattr(animal, k)) for k in animal_keys}
        return JsonResponse(animal_data)
