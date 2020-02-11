from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:noticia_id>', views.noticia, name='noticia'),
]