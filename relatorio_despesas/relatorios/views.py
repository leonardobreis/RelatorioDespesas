from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Especifique o template a ser usado

def custom_login_view(request):
    return auth_views.LoginView.as_view(template_name='registration/login.html')(request)

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redireciona para a página de login
    return render(request, 'home.html')
    #return HttpResponse("Bem-vindo à página inicial!")
