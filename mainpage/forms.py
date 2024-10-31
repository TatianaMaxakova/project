from django import forms
from . import models

class VisitForm(forms.ModelForm):
    class Meta:
        model = models.Visit
        #fields = [field.name for field in Task._meta.get_fields()]
        fields = [
            'executor',
            'color',
            'start_time'
        ]
        #labels = {
        #    "given": "Задача выдана",
        #}
        widgets = {
            'color': forms.TextInput(attrs={'type':'color'}),
            'start_time': forms.DateInput(attrs={'type':'datetime-local'}),
        }