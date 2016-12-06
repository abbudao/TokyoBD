from django import forms
from .models import HabilitadoArbitrar
class HabilitadoForm(forms.ModelForm):
    class Meta:
        model = HabilitadoArbitrar
        fields =('codigo','esporte',)
