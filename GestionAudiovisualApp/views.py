from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import TipoEquipo, Marca, Modelo, TecnologiaConexion
from django.urls import reverse_lazy
from django import forms
from django.db.models import Q  # Para manejar consultas complejas

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
