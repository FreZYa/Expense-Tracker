from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['name', 'formatted_amount', 'category', 'date', 'created_at']
    list_filter = ['category', 'date', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['-date', '-created_at']
    date_hierarchy = 'date'
    list_per_page = 25
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'amount', 'category', 'date')
        }),
        ('Detaylar', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
        ('Sistem Bilgileri', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related()
    
    def formatted_amount(self, obj):
        return obj.formatted_amount
    formatted_amount.short_description = 'Tutar'
    formatted_amount.admin_order_field = 'amount'