from django.shortcuts import render, redirect
from bank_account.dao.bankAccountDao import BankAccountDao

bank_account_dao = BankAccountDao()


def add_bank_account(request):
    if request.method == 'POST':
        bank_name = request.POST.get('bank_name')
        opening_balance = request.POST.get('opening_balance')
        try:
            bank_account = bank_account_dao.add_bank_account(bank_name, opening_balance)
            return redirect('add_transaction')
        except Exception as e:
            return render(request, 'add_bank_account.html', {'error': str(e)})
    else:
        return render(request, 'bank_account/add_bank_account.html')


def list_banks(request):
    banks = bank_account_dao.get_all_banks_ordered_by_balance()
    context = {
        'banks': banks,
    }
    return render(request, 'bank_account/view_bank_accounts.html', context)
