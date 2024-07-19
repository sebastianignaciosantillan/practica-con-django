from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate

def registrarse(request):
    if request.method == 'POST':
        user_creation_form = NewUserForm(data=request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save()  # Guarda el nuevo usuario
            # Autenticación inmediata del nuevo usuario
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            if user is not None:  # Verifica que la autenticación fue exitosa
                login(request, user)
                return redirect('index')  # Redirige a la página de inicio
        else:
            # Si el formulario no es válido, vuelve a mostrar el formulario con errores
            data = {
                'form': user_creation_form
            }
    else:
        # Si la solicitud no es POST, muestra el formulario vacío
        user_creation_form = NewUserForm()
        data = {
            'form': user_creation_form
        }

    return render(request, 'registrarse.html', data)
