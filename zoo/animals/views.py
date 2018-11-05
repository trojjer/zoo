from django.views.generic import View
from django.views.generic.base import HttpResponse

from .models import Animal


class AnimalPopulationView(View):
    """Show a count of the current zoo population.
    """
    def get(self, *args, **kwargs):
        return HttpResponse(Animal.objects.count())
