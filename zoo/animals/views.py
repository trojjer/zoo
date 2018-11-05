from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.forms import ValidationError

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
        animal_name = request.GET.get('name')
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
