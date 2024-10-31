from django import forms
from .models import Modelo, Marca, Equipo, TipoEquipo, Usuario, Empleado

class ModeloForm(forms.ModelForm):
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione una marca"
    )
    class Meta:
        model = Modelo
        fields = ['marca', 'descripcion', 'estado']


class EquipoForm(forms.ModelForm):
    tipo_equipo = forms.ModelChoiceField(
        queryset= TipoEquipo.objects.values_list('descripcion', flat=True),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione un Tipo Equipo"
    )
    class Meta:
        model = Equipo
        fields = ['descripcion', 'numero_serial', 'service_tag', 'tipo_equipo', 'marca', 'modelo', 'tecnologia_conexion', 'estado']


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'cedula', 'numero_carnet', 'tipo_usuario', 'tipo_persona', 'estado']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'cedula', 'tanda_labor', 'fecha_ingreso', 'estado']