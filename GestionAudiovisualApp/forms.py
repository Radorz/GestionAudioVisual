from django import forms
from .models import Modelo, Marca

class ModeloForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione una marca"
    )

    class Meta:
        model = Modelo
        fields = ['marca', 'descripcion', 'estado']
