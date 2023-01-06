from logging import getLogger

from django import forms
from django.core.exceptions import ValidationError
from django.forms import Form, Textarea, ModelForm

from base.models import Room

LOGGER = getLogger()  ##2.


class RoomForm(ModelForm):  ##1. Form 2.ModelForm
    ##1. možnost
    # name = forms.CharField(max_length=200, validators=[muj_validator])
    # description = forms.CharField(widget=Textarea, required=False)
    # def muj_validator(value):
    ##2. možnost
    class Meta:
        model = Room
        field = '__all__'
        exclude = ['participants']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            validation_error = "Jmeno musí obsahovat min. 2 znaky"
            LOGGER.warning(f'{name}: {validation_error} ')
            raise ValidationError(validation_error)
        return name.capitalize()
