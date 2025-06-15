from django import forms
from django.forms import ModelForm
from .models import Expense
from datetime import date

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'category', 'description', 'date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Harcama adını girin...'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'İsteğe bağlı açıklama...',
                'rows': 3
            }),
            'date': forms.DateInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'type': 'date'
            }),
        }
        labels = {
            'name': 'Harcama Adı',
            'amount': 'Tutar (TL)',
            'category': 'Kategori',
            'description': 'Açıklama',
            'date': 'Tarih',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Yeni kayıt için bugünün tarihini varsayılan yap
            self.fields['date'].initial = date.today()
        
        # Tüm alanları gerekli yap, açıklama hariç
        for field_name, field in self.fields.items():
            if field_name != 'description':
                field.required = True