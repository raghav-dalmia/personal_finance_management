from decimal import Decimal
from bank_transactions.models import Transaction
from bank_account.dao.bankAccountDao import BankAccountDao
from bank_transactions.dao.transactionLabelDAO import TransactionLabelDAO

bank_account_dao = BankAccountDao()
transaction_label_dao = TransactionLabelDAO()


class TransactionDAO:

    def add_transaction(self, bank_id, transaction_details, transaction_date, transaction_type, amount, label_name):
        amount = Decimal(str(amount))
        bank_account = bank_account_dao.get_bank_account_by_id(bank_id)
        if label_name is not None and len(label_name) > 0:
            label = transaction_label_dao.get_or_create_label(label_name)
        else:
            label = None
        Transaction.objects.create(
            bank=bank_account,
            transaction_details=transaction_details,
            transaction_date=transaction_date,
            transaction_type=transaction_type,
            amount=amount,
            label=label
        )

    def get_transactions_by_bank_and_type(self, bank_id, transaction_type=None) -> list:
        bank_account = bank_account_dao.get_bank_account_by_id(bank_id)
        queryset = Transaction.objects.filter(bank=bank_account)
        if transaction_type:
            queryset = queryset.filter(transaction_type=transaction_type)
        return queryset.order_by('-transaction_date')
