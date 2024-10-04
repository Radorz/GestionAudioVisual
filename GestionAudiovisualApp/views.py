from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TipoEquipo, Marca, Modelo, TecnologiaConexion
from django.urls import reverse_lazy
from django import forms
from django.db.models import Q  # Para manejar consultas complejas
from .forms import ModeloForm

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
    fields = ['nombre', 'estado']
    template_name = 'tecnologia-conexion/tecnologiaconexion_form.html'
    success_url = reverse_lazy('tecnologiaconexion-list')

class TecnologiaConexionUpdateView(UpdateView):
    model = TecnologiaConexion
    fields = ['nombre', 'estado']
    template_name = 'tecnologia-conexion/tecnologiaconexion_form.html'
    success_url = reverse_lazy('tecnologiaconexion-list')

class TecnologiaConexionDeleteView(DeleteView):
    model = TecnologiaConexion
    template_name = 'tecnologia-conexion/tecnologiaconexion_confirm_delete.html'
    success_url = reverse_lazy('tecnologiaconexion-list')