from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, LoginForm, ProfileForm, CustomPasswordChangeForm
from .models import *
from .forms import *

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        ProfileModel.objects.create(user=user)
        return redirect('login')
    return render(request, 'myapp/Auth/register.html', {'form': form})


def login_view(request):
    form = LoginForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('profile')
    return render(request, 'myapp/Auth/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    profile, created = ProfileModel.objects.get_or_create(user=request.user)
    return render(request, 'myapp/Auth/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile, created = ProfileModel.objects.get_or_create(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    if form.is_valid():
        form.save()
        return redirect('profile')

    return render(request, 'myapp/master/master_form.html', {
        'form': form,
        'Title': 'Edit Profile',
        'submit_btn': 'Update'
    })


@login_required
def change_password_view(request):
    form = CustomPasswordChangeForm(user=request.user, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'myapp/master/master_form.html', {
        'form': form,
        'Title': 'Change Password',
        'submit_btn': 'Update Password'
    })



@login_required
def Cash_List(request):
    cash_list=AddCashModel.objects.all()
    return render(request, 'crud/dashboard.html', {'cash_list': cash_list})


@login_required
def Add_cash(request):
    
    if request.method == 'POST':
        form = AddCashForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('Dashboard')
    else:
        form = AddCashForm()
    return render(request, 'myapp/master/master_form.html', {
        'form': form,
        'Title': "Add new Cash",
        'submit_btn': "Submit",
        })


from django.shortcuts import get_object_or_404

@login_required
def Edit_cash(request, pk):
    cash = get_object_or_404(AddCashModel, pk=pk, user=request.user)

    if request.method == 'POST':
        form = AddCashForm(request.POST, instance=cash)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = AddCashForm(instance=cash)

    return render(request, 'myapp/master/master_form.html', {
        'form': form,
        'Title': "Edit Cash",
        'submit_btn': "Update",
    })
    


@login_required
def Delete_cash(request, pk):
    get_object_or_404(AddCashModel, pk=pk, user=request.user).delete()
    return redirect('Dashboard')


@login_required
def Expense_List(request):
    expense_list=ExpenseModel.objects.all()
    return render(request, 'crud/dashboard.html', {'expense_list': expense_list})



@login_required
def Add_expense(request):
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('Dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'myapp/master/master_form.html', {
        'form': form,
        'Title': "Add new expense",
        'submit_btn': "Submit",
        })
    
    
@login_required
def Edit_expense(request, pk):
    expense = get_object_or_404(ExpenseModel, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('Dashboard')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'myapp/master/master_form.html', {
        'form': form,
        'Title': "Edit Expense",
        'submit_btn': "Update",
    })
    
@login_required
def Delete_expense(request, pk):
    get_object_or_404(ExpenseModel, pk=pk, user=request.user).delete()
    return redirect('Dashboard')    
    
    
@login_required
def Dashboard(request):
    cash = AddCashModel.objects.filter(user=request.user)
    expense = ExpenseModel.objects.filter(user=request.user)

    total_cash = sum(c.amount for c in cash)
    total_expense = sum(e.amount for e in expense)
    balance = total_cash - total_expense

    context = {
        'cash': cash,
        'expense': expense,
        'total_cash': total_cash,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request,'crud/dashboard.html', context)