from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview, name='index'),
    path('crear/', views.crear_fruta, name='crear'),
    path('listar/', views.listar_frutas, name='listar'),
    path('actualizar/<int:pk>/', views.actualizar_fruta, name='actualizar'),
     path('eliminar/<int:pk>/', views.eliminar_fruta, name='eliminar'),
]