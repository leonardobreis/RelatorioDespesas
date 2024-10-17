from django import forms
from .models import RelatorioDespesa

class RelatorioDespesaForm(forms.ModelForm):
    class Meta:
        model = RelatorioDespesa
        fields = ['descricao', 'valor', 'data']
