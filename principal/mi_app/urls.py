from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo_autor/', login_required(views.nuevo_autor), name='nuevo_autor'),
    path('nuevo_libro/<int:autor_id>/', login_required(views.nuevo_libro), name='nuevo_libro'),
    path('editar_autor/<int:autor_id>/<int:libro_id>/', login_required(views.editar_autor), name='editar_autor'),
    path('eliminar_autor/<int:autor_id>/', login_required(views.eliminar_autor), name='eliminar_autor'),
    path('listado/', login_required(views.listado), name='listado'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

