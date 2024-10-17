# relatorio_despesas/relatorios/urls.py
from django.urls import path
from .views import custom_login_view, home

urlpatterns = [
    path('', home, name='home'),
    path('login/', custom_login_view, name='login'),
]
