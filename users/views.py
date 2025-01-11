# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']  # Guardar el nombre
            user.last_name = form.cleaned_data['last_name']  # Guardar el apellido
            user.save()
            # login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# Vista de Inicio de Sesión
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirige a la página de inicio
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

# Vista de Dashboard
@login_required
def dashboard_view(request):
    return render(request, 'home/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
