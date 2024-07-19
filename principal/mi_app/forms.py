from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'edad']
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class':'input'}
            ), 
            'edad': forms.TextInput(
                attrs={'class':'input'}
            ), 
        }
        
        
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro        
        fields = ['titulo', 'descripcion', 'fecha_publicacion', 'genero', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input'}),
            'descripcion': forms.Textarea(attrs={'class': 'textarea'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'image'})
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['imagen'].required = False

