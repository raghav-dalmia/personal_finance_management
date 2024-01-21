from django.contrib import admin
from django.urls import path, include
from bank_transactions.views import add_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_transaction, name='home'),
    path('transaction/', include('bank_transactions.urls')),
    path('bank/', include('bank_account.urls')),
]
