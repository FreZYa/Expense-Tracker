from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
from datetime import datetime, date, timedelta

# Create your views here.
def index(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
    expense_form = ExpenseForm()
    # total expenses
    expenses = Expense.objects.all()
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum']
    # 365 days expenses
    last_year = date.today() - timedelta(days=365)
    expenses = expenses.filter(date__gte=last_year)
    yearly_sum = expenses.aggregate(Sum('amount'))['amount__sum']
    # 30 days expenses
    last_month = date.today() - timedelta(days=30)
    expenses = expenses.filter(date__gte=last_month)
    monthly_sum = expenses.aggregate(Sum('amount'))['amount__sum']
    # 7 days expenses
    last_week = date.today() - timedelta(days=7)
    expenses = expenses.filter(date__gte=last_week)
    weekly_sum = expenses.aggregate(Sum('amount'))['amount__sum']
    # 1 day expenses
    daily_sums = expenses.values('date').annotate(total_amount=Sum('amount'))
    print("daily_sums", daily_sums)
    return render(request, 'index.html', {
        'expense_form': expense_form, 
        'expenses': expenses, 
        'total_expenses': total_expenses or 0,
        'yearly_sum': yearly_sum or 0,
        'monthly_sum': monthly_sum or 0,
        'weekly_sum': weekly_sum or 0,
        'daily_sums': daily_sums or 0})

def edit(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit.html', {'form': form})

def delete(request, id):
    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        expense.delete()
        return redirect('index')
    return render(request, 'delete.html')