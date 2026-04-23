from django.urls import path
from .views import *

urlpatterns = [
    path('', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('change-password/', change_password_view, name='change_password_view'),
    
    
    path('Cash_List/', Cash_List, name='Cash_List'),
    path('Add_cash/', Add_cash, name='Add_cash'),
    path('Expense_List/', Expense_List, name='Expense_List'),
    path('Add_expense/', Add_expense, name='Add_expense'),
    
    
    path('Dashboard/', Dashboard, name='Dashboard'),
    
    path('cash/edit/<int:pk>/', Edit_cash, name='edit_cash'),
    path('cash/delete/<int:pk>/', Delete_cash, name='delete_cash'),

    path('expense/edit/<int:pk>/', Edit_expense, name='edit_expense'),
    path('expense/delete/<int:pk>/', Delete_expense, name='delete_expense'),
]
