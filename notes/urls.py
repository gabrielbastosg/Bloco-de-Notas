from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='lista-notas'),
    path('nova/',views.create_note,name='criar-notas'),
    path('editar/<int:id>/', views.edit_note, name='editar-nota'),
    path('deletar/<int:id>/', views.delete_note, name='deletar-nota'),
]