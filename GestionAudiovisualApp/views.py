from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TipoEquipo, Marca, Modelo, TecnologiaConexion, Equipo, Usuario, Empleado
from django.urls import reverse_lazy
from django import forms
from django.db.models import Q  # Para manejar consultas complejas
from .forms import ModeloForm, EquipoForm, UsuarioForm, EmpleadoForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')
# CRUD para TipoEquipo
class TipoEquipoListView(ListView):
    model = TipoEquipo
    template_name = 'tipos-equipos/tipoequipo_list.html'
    context_object_name = 'tipos'  # Cambiar el nombre en el contexto
    paginate_by = 10  # Si quieres paginación, puedes agregar esto

    def get_queryset(self):
        queryset = TipoEquipo.objects.all()
        query = self.request.GET.get('q')  # Obtener el término de búsqueda
        if query:
            queryset = queryset.filter(
                Q(descripcion__icontains=query)  # Buscar por descripción
            )
        return queryset

class TipoEquipoCreateView(CreateView):
    model = TipoEquipo
    fields = ['descripcion', 'estado']
    template_name = 'tipos-equipos/tipoequipo_form.html'
    success_url = reverse_lazy('tipoequipo-list')
    widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TipoEquipoUpdateView(UpdateView):
    model = TipoEquipo
    fields = [ 'descripcion', 'estado']
    template_name = 'tipos-equipos/tipoequipo_form.html'
    success_url = reverse_lazy('tipoequipo-list')

class TipoEquipoDeleteView(DeleteView):
    model = TipoEquipo
    template_name = 'tipos-equipos/tipoequipo_confirm_delete.html'
    success_url = reverse_lazy('tipoequipo-list')

class MarcaListView(ListView):
    model = Marca
    template_name = 'marcas/marca_list.html'
    context_object_name = 'marcas'
    def get_queryset(self):
        queryset = Marca.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query)
            )
        return queryset

class MarcaCreateView(CreateView):
    model = Marca
    fields = ['descripcion', 'estado']
    template_name = 'marcas/marca_form.html'
    success_url = reverse_lazy('marca-list')

class MarcaUpdateView(UpdateView):
    model = Marca
    fields = ['descripcion', 'estado']
    template_name = 'marcas/marca_form.html'
    success_url = reverse_lazy('marca-list')

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'marcas/marca_confirm_delete.html'
    success_url = reverse_lazy('marca-list')

# Modelo Views
class ModeloListView(ListView):
    model = Modelo
    template_name = 'modelos/modelo_list.html'
    context_object_name = 'modelos'
    def get_queryset(self):
        queryset = Modelo.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) | Q(marca__descripcion__icontains=query)
            )
        return queryset

class ModeloCreateView(CreateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'modelos/modelo_form.html'
    success_url = reverse_lazy('modelo-list')

class ModeloUpdateView(UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'modelos/modelo_form.html'
    success_url = reverse_lazy('modelo-list')
    
class ModeloDeleteView(DeleteView):
    model = Modelo
    template_name = 'modelos/modelo_confirm_delete.html'
    success_url = reverse_lazy('modelo-list')

# Tecnología de Conexión Views
class TecnologiaConexionListView(ListView):
    model = TecnologiaConexion
    template_name = 'tecnologia-conexion/tecnologiaconexion_list.html'
    context_object_name = 'tecnologias'

class TecnologiaConexionCreateView(CreateView):
    model = TecnologiaConexion
    fields = ['descripcion', 'estado']
    template_name = 'tecnologia-conexion/tecnologiaconexion_form.html'
    success_url = reverse_lazy('tecnologiaconexion-list')

class TecnologiaConexionUpdateView(UpdateView):
    model = TecnologiaConexion
    fields = ['descripcion', 'estado']
    template_name = 'tecnologia-conexion/tecnologiaconexion_form.html'
    success_url = reverse_lazy('tecnologiaconexion-list')

class TecnologiaConexionDeleteView(DeleteView):
    model = TecnologiaConexion
    template_name = 'tecnologia-conexion/tecnologiaconexion_confirm_delete.html'
    success_url = reverse_lazy('tecnologiaconexion-list')

class EquipoListView(ListView):
    model = Equipo
    template_name = 'equipos/equipo_list.html'
    context_object_name = 'equipos'

# Vista para crear un nuevo Equipo
class EquipoCreateView(CreateView):
    model = Equipo,
    form_class = EquipoForm
    template_name = 'equipos/equipo_form.html'
    # fields = ['descripcion', 'numero_serial', 'service_tag', 'tipo_equipo', 'marca', 'modelo', 'tecnologia_conexion', 'estado']
    success_url = reverse_lazy('equipo-list')

# Vista para actualizar un Equipo existente
class EquipoUpdateView(UpdateView):
    model = Equipo
    template_name = 'equipos/equipo_form.html'
    fields = ['descripcion', 'numero_serial', 'service_tag', 'tipo_equipo', 'marca', 'modelo', 'tecnologia_conexion', 'estado']
    success_url = reverse_lazy('equipo-list')

# Vista para eliminar un Equipo
class EquipoDeleteView(DeleteView):
    model = Equipo
    template_name = 'equipos/equipo_confirm_delete.html'
    success_url = reverse_lazy('equipo-list')

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario-list')

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado-list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado-list')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado-list')