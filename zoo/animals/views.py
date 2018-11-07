from datetime import timedelta

from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import Animal
from .forms import AnimalModelForm


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
    form_class = AnimalModelForm

    def get(self, request, *args, **kwargs):
        """Retrieve Animal by name, if it exists.
        """
        animal_name = kwargs.get('name')
        animal = get_object_or_404(self.model, name=animal_name)
        return self._get_json_response(animal)

    def post(self, request, *args, **kwargs):
        """Create a new animal if the form data is valid.
        """
        form = self.form_class(data=self.request.POST)

        if form.is_valid():
            response = self._get_json_response(form.save())
            response.status_code = 401
            return response

        return HttpResponse(status=422, content=f'Errors: {form.errors}')

    def _get_json_response(self, animal):
        """
        Convenience method for animal object JSON serialisation.
        Accounts for datetime field.
        Returns a JsonResponse instance (which itself uses DjangoJSONEncoder).
        """
        animal_keys = ['name', 'species', 'last_feed_time']
        animal_data = {k: str(getattr(animal, k)) for k in animal_keys}
        return JsonResponse(animal_data)


class HungryAnimalsView(View):
    """Show a count of the animals which haven't been fed for at least 2 days.
    """
    model = Animal

    def get(self, *args, **kwargs):
        hungry_filter = {
            'last_feed_time__lte': timezone.now() - timedelta(days=2)
        }
        hungry_count = self.model.objects.filter(**hungry_filter).count()
        return HttpResponse(hungry_count)


class FeedAnimalView(View):
    """Feed an Animal: Update its last_feed_time to the current time.
    """
    model = Animal

    def post(self, request, *args, **kwargs):
        animal_name = request.POST.get('name')
        try:
            animal = self.model.objects.get(name=animal_name)
        except self.model.DoesNotExist:
            return HttpResponse(
                status=422,
                content=f'Could not find Animal named {animal_name}'
            )

        animal.last_feed_time = timezone.now()
        animal.save()
        return HttpResponse(status=204)
