from venv import logger
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario  
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
# Create your views here.

# start view
def home(request):
    return render (request, 'users/home.html')

def createUser(request):
    pass