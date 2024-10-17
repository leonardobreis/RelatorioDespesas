# relatorio_despesas/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relatorios.urls')),
    path('login/', include('relatorios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
