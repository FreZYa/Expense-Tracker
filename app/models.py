from django.db import models
from decimal import Decimal

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Yiyecek & İçecek'),
        ('transport', 'Ulaşım'),
        ('entertainment', 'Eğlence'),
        ('utilities', 'Faturalar'),
        ('shopping', 'Alışveriş'),
        ('health', 'Sağlık'),
        ('education', 'Eğitim'),
        ('housing', 'Konut'),
        ('clothing', 'Giyim'),
        ('other', 'Diğer'),
    ]
    
    name = models.CharField(max_length=255, verbose_name="Harcama Adı")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Tutar")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other', verbose_name="Kategori")
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    date = models.DateField(verbose_name="Tarih")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = "Harcama"
        verbose_name_plural = "Harcamalar"

    def __str__(self):
        return f"{self.name} - {self.amount} TL"

    @property
    def formatted_amount(self):
        return f"{self.amount:,.2f} TL"
