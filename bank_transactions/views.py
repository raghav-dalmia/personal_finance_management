from django.shortcuts import render, redirect
from bank_transactions.dao.transactionDAO import TransactionDAO
from bank_account.dao.bankAccountDao import BankAccountDao
from bank_transactions.dao.transactionLabelDAO import TransactionLabelDAO

transaction_dao = TransactionDAO()
bank_account_dao = BankAccountDao()
label_dao = TransactionLabelDAO()


def add_transaction(request):
    if request.method == 'POST':
        bank_account_id = request.POST.get('bank_account')
        transaction_type = request.POST.get('transaction_type', 'debit')
        transaction_details = request.POST.get('transaction_details').strip()
        amount = request.POST.get('amount')
        transaction_date = request.POST.get('transaction_date')
        label_name = request.POST.get('label').strip()

        try:
            transaction_dao.add_transaction(
                bank_account_id, transaction_details, transaction_date, transaction_type, amount, label_name
            )
            return redirect('add_transaction')
        except Exception as e:
            banks = bank_account_dao.get_all_banks_ordered_by_balance()
            return render(request, 'bank_transactions/add_transaction.html', {
                'error': str(e),
                'banks': banks
            })
    else:
        banks = bank_account_dao.get_all_banks_ordered_by_balance()
        return render(request, 'bank_transactions/add_transaction.html', {'banks': banks})


def view_transactions(request):
    bank_name = request.GET.get('bank_name')
    error_message, selected_bank, transactions = "", None, []
    banks = bank_account_dao.get_all_banks_ordered_by_balance()
    if bank_name:
        try:
            selected_bank = next(bank for bank in banks if bank.bank_name == bank_name)
            transactions = transaction_dao.get_transactions_by_bank_and_type(selected_bank.id)
        except StopIteration:
            error_message = "Bank not found."
    elif len(banks) > 0:
        selected_bank = banks[0]
        transactions = transaction_dao.get_transactions_by_bank_and_type(selected_bank.id)
    else:
        error_message = "Bank not found."

    return render(request, 'bank_transactions/view_transactions.html', {
        'banks': banks,
        'transactions': transactions,
        'selected_bank': selected_bank,
        'error': error_message
    })
