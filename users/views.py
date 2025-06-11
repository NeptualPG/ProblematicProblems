import logging; 
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import User  
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

# start view
def home(request):
    return render (request, 'users/home.html')

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Tu cuenta ha sido creada y has iniciado sesión exitosamente!')
            return redirect('home')
        # In case of error
        else:
            messages.error(request, _('Error en el formulario. Verifica los datos.'))
    else:
        form = CustomUserCreationForm()
        
    # GET
    return render(request, 'users/create_user.html', {'form' : form})
