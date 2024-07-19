from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    
    return render(request, 'index.html',{})


def listado(request):
    queryset = request.GET.get('buscar')
    if queryset:
        autores = Autor.objects.filter(
            Q(nombre__icontains=queryset)
        ).prefetch_related('libro')
    else:
        autores = Autor.objects.all().prefetch_related('libro')
    
   
    
    return render(request, 'listado.html', {'autores': autores})

def nuevo_autor(request):
    if request.method == 'POST':
        form_autor = AutorForm(request.POST)
        form_libro = LibroForm(request.POST)
        if form_libro.is_valid() and form_autor.is_valid():
            autor = form_autor.save() #persistir. exista el id
            libro = form_libro.save(commit =False) #instancia incompleta
            libro.autor = autor
            libro.save() # persiste finalmente
            return redirect('listado')
            
    else:
        form_autor = AutorForm()
        form_libro = LibroForm()
    return render(request, 'nuevo_autor.html', {'form_autor':form_autor, 'form_libro':form_libro})


def nuevo_libro(request, autor_id):
    autor = Autor.objects.get(id = autor_id)
    if request.method == 'POST':
        form_libro = LibroForm(request.POST)
        if form_libro.is_valid():
            libro = form_libro.save(commit =False) #instancia incompleta
            libro.autor = autor
            libro.save() # persiste finalmente
            return redirect('listado')
            
    else:
        form_libro = LibroForm()
    return render(request, 'nuevo_libro.html', {'form_libro':form_libro})

def editar_autor(request, autor_id, libro_id):
    autor = get_object_or_404(Autor, id=autor_id)
    libro = get_object_or_404(Libro, id= libro_id)

    if request.method == 'POST':
        form_autor = AutorForm(request.POST, instance=autor)
        form_libro = LibroForm(request.POST, instance=libro)
        if form_libro.is_valid() and form_autor.is_valid():
            form_autor.save()
            form_libro.save()
            return redirect('listado')
    else:
        form_autor = AutorForm(instance=autor)
        form_libro = LibroForm(instance=libro)

    return render(request, 'editar_autor.html', {'form_autor': form_autor, 'form_libro': form_libro})

def eliminar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('listado')
    else:
        return render(request, 'confirmacion_delete.html', {'autor': autor})