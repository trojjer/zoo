from django.forms.models import ModelForm
from django import forms

from .models import Animal


class AnimalModelForm(ModelForm):
    """Form to validate request data and create an Animal.
    """
    def clean_name(self):
        name = self.cleaned_data['name']
        if self.Meta.model.objects.filter(name=name).count():
            raise forms.ValidationError('Cannot create Animal with duplicate name.')
        return name

    class Meta:
        model = Animal
        fields = ['name', 'species',]
