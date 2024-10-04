"""
URL configuration for GestionAudiovisual project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GestionAudiovisualApp.views import ( inicio,TipoEquipoListView, TipoEquipoCreateView, TipoEquipoUpdateView, TipoEquipoDeleteView,                                         
    MarcaListView, MarcaCreateView, MarcaUpdateView, MarcaDeleteView,
    ModeloListView, ModeloCreateView, ModeloUpdateView, ModeloDeleteView,
    TecnologiaConexionListView, TecnologiaConexionCreateView, TecnologiaConexionUpdateView, TecnologiaConexionDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  
    path('tipos/', TipoEquipoListView.as_view(), name='tipoequipo-list'),
    path('tipos/new/', TipoEquipoCreateView.as_view(), name='tipoequipo-create'),
    path('tipos/edit/<int:pk>/', TipoEquipoUpdateView.as_view(), name='tipoequipo-update'),
    path('tipos/delete/<int:pk>/', TipoEquipoDeleteView.as_view(), name='tipoequipo-delete'),

      # CRUD de Marca
    path('marcas/', MarcaListView.as_view(), name='marca-list'),
    path('marcas/new/', MarcaCreateView.as_view(), name='marca-create'),
    path('marcas/update/<int:pk>/', MarcaUpdateView.as_view(), name='marca-update'),
    path('marcas/delete/<int:pk>/', MarcaDeleteView.as_view(), name='marca-delete'),

    # CRUD de Modelo
    path('modelos/', ModeloListView.as_view(), name='modelo-list'),
    path('modelos/new/', ModeloCreateView.as_view(), name='modelo-create'),
    path('modelos/update/<int:pk>/', ModeloUpdateView.as_view(), name='modelo-update'),
    path('modelos/delete/<int:pk>/', ModeloDeleteView.as_view(), name='modelo-delete'),

    # CRUD de Tecnología de Conexión
    path('tecnologias/', TecnologiaConexionListView.as_view(), name='tecnologiaconexion-list'),
    path('tecnologias/new/', TecnologiaConexionCreateView.as_view(), name='tecnologiaconexion-create'),
    path('tecnologias/update/<int:pk>/', TecnologiaConexionUpdateView.as_view(), name='tecnologiaconexion-update'),
    path('tecnologias/delete/<int:pk>/', TecnologiaConexionDeleteView.as_view(), name='tecnologiaconexion-delete'),
]
