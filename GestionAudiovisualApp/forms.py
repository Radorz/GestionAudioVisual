from django import forms
from .models import Modelo, Marca, Equipo, TipoEquipo, Usuario, Empleado, Prestamo

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
        queryset= TipoEquipo.objects.all(),
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
        widgets = {
        'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class PrestamoForm(forms.ModelForm):
    empleado = forms.ModelChoiceField(
        queryset= Empleado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione Empledo"
    )
    equipo = forms.ModelChoiceField(
        queryset= Equipo.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione Equipo"
    )
    usuario = forms.ModelChoiceField( 
        queryset= Usuario.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Seleccione Usuario"
    )
    class Meta:
        model = Prestamo
        fields = ['empleado', 'equipo', 'usuario', 'fecha_prestamo']
        widgets = {
        'fecha_prestamo': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        'fecha_devolucion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }



class DevolverPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_devolucion', 'comentario']
        widgets = {
        'fecha_devolucion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('fecha_devolucion'):
            raise forms.ValidationError("Debe registrar una fecha de devolución.")
        return cleaned_data


class ConsultaCriteriosForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=Usuario.objects.all(), required=False, label="Usuario")
    equipo = forms.ModelChoiceField(queryset=Equipo.objects.all(), required=False, label="Equipo")
    fecha_inicio = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha Inicio")
    fecha_fin = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha Fin")
    tipo_equipo = forms.ModelChoiceField(queryset=TipoEquipo.objects.all(), required=False, label="Tipo de Equipo")