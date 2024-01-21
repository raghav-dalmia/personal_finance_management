from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_bank_account, name='add_bank_account'),
    path('view/', views.list_banks, name='list_banks'),
]