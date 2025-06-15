from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from datetime import datetime, date, timedelta
from .forms import ExpenseForm
from .models import Expense

# Create your views here.
def index(request):
    """Ana sayfa - harcama ekleme ve listeleme"""
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            messages.success(request, 'Harcama başarıyla eklendi!')
            return redirect('index')
        else:
            messages.error(request, 'Lütfen form bilgilerini kontrol edin.')
    else:
        expense_form = ExpenseForm()
    
    # Filtreleme seçenekleri
    filter_days = request.GET.get('filter', '30')
    try:
        filter_days = int(filter_days)
    except ValueError:
        filter_days = 30
    
    # Temel sorgu
    expenses = Expense.objects.all().select_related()
    
    # Toplam harcamalar
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Filtrelenmiş harcamalar - kategori analizi için tüm verileri kullan
    filtered_expenses = expenses  # Tüm veriyi kullan, zaman filtresi yok
    
    # İstatistikler
    stats = calculate_expense_stats(expenses)
    
    # Günlük toplamlar (son 30 gün)
    last_30_days = date.today() - timedelta(days=30)
    daily_sums = expenses.filter(date__gte=last_30_days).values('date').annotate(
        total_amount=Sum('amount')
    ).order_by('-date')[:30]
    
    # Kategori renk eşleştirmesi
    CATEGORY_COLORS = {
        'food': {'color': '#EF4444', 'bg_class': 'bg-red-500', 'text_class': 'text-red-600'},
        'transport': {'color': '#3B82F6', 'bg_class': 'bg-blue-500', 'text_class': 'text-blue-600'},
        'entertainment': {'color': '#8B5CF6', 'bg_class': 'bg-purple-500', 'text_class': 'text-purple-600'},
        'utilities': {'color': '#F59E0B', 'bg_class': 'bg-yellow-500', 'text_class': 'text-yellow-600'},
        'shopping': {'color': '#EC4899', 'bg_class': 'bg-pink-500', 'text_class': 'text-pink-600'},
        'health': {'color': '#10B981', 'bg_class': 'bg-green-500', 'text_class': 'text-green-600'},
        'education': {'color': '#06B6D4', 'bg_class': 'bg-cyan-500', 'text_class': 'text-cyan-600'},
        'housing': {'color': '#84CC16', 'bg_class': 'bg-lime-500', 'text_class': 'text-lime-600'},
        'clothing': {'color': '#F97316', 'bg_class': 'bg-orange-500', 'text_class': 'text-orange-600'},
        'other': {'color': '#6B7280', 'bg_class': 'bg-gray-500', 'text_class': 'text-gray-600'},
    }
    
    # Kategori toplamları
    categorical_sums = filtered_expenses.values(
        'category'
    ).annotate(
        total_amount=Sum('amount'),
        count=Count('id')
    ).order_by('-total_amount')
    
    # Kategorilere renk bilgisi ekle
    categorical_sums_with_colors = []
    for cat_sum in categorical_sums:
        cat_data = dict(cat_sum)
        cat_data.update(CATEGORY_COLORS.get(cat_sum['category'], CATEGORY_COLORS['other']))
        categorical_sums_with_colors.append(cat_data)
    
    # Sayfalama
    paginator = Paginator(filtered_expenses, 10)
    page_number = request.GET.get('page')
    expenses_page = paginator.get_page(page_number)
    
    context = {
        'expense_form': expense_form, 
        'expenses': expenses_page, 
        'total_expenses': total_expenses,
        'yearly_sum': stats['yearly_sum'],
        'monthly_sum': stats['monthly_sum'],
        'weekly_sum': stats['weekly_sum'],
        'daily_sums': daily_sums,
        'categorical_sums': categorical_sums_with_colors,
        'category_colors': CATEGORY_COLORS,
        'filter_days': filter_days,
        'stats': stats,
    }
    
    return render(request, 'index.html', context)

def calculate_expense_stats(expenses):
    """Harcama istatistiklerini hesapla"""
    today = date.today()
    
    # Farklı zaman aralıkları
    last_year = today - timedelta(days=365)
    last_month = today - timedelta(days=30)
    last_week = today - timedelta(days=7)
    
    stats = {
        'yearly_sum': expenses.filter(date__gte=last_year).aggregate(Sum('amount'))['amount__sum'] or 0,
        'monthly_sum': expenses.filter(date__gte=last_month).aggregate(Sum('amount'))['amount__sum'] or 0,
        'weekly_sum': expenses.filter(date__gte=last_week).aggregate(Sum('amount'))['amount__sum'] or 0,
        'total_count': expenses.count(),
        'monthly_count': expenses.filter(date__gte=last_month).count(),
        'avg_daily': 0,
    }
    
    # Günlük ortalama hesapla
    if stats['monthly_sum'] > 0:
        stats['avg_daily'] = stats['monthly_sum'] / 30
    
    return stats

def edit(request, id):
    """Harcama düzenleme"""
    expense = get_object_or_404(Expense, id=id)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Harcama başarıyla güncellendi!')
            return redirect('index')
        else:
            messages.error(request, 'Lütfen form bilgilerini kontrol edin.')
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'edit.html', {
        'form': form, 
        'expense': expense
    })

def delete(request, id):
    """Harcama silme"""
    expense = get_object_or_404(Expense, id=id)
    
    if request.method == 'POST':
        expense_name = expense.name
        expense.delete()
        messages.success(request, f'"{expense_name}" harcaması başarıyla silindi!')
        return redirect('index')
    
    return render(request, 'delete.html', {'expense': expense})

def expense_chart_data(request):
    # Kategori verileri
    category_data = Expense.objects.values('category').annotate(
        total=Sum('amount')
    ).order_by('-total')
    
    # Son 30 günün günlük verileri
    last_30_days = date.today() - timedelta(days=30)
    daily_data = Expense.objects.filter(date__gte=last_30_days).values('date').annotate(
        total=Sum('amount')
    ).order_by('date')
    
    return JsonResponse({
        'categories': {
            'labels': [item['category'] for item in category_data],
            'data': [float(item['total']) for item in category_data]
        },
        'daily': {
            'labels': [item['date'].strftime('%d/%m') for item in daily_data],
            'data': [float(item['total']) for item in daily_data]
        }
    })