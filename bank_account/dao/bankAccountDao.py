from bank_transactions.models import BankAccount


class BankAccountDao:

    def add_bank_account(self, bank_name, opening_balance):
        bank_account = BankAccount.objects.create(
            bank_name=bank_name,
            opening_balance=opening_balance
        )
        return bank_account

    def get_all_banks_ordered_by_balance(self):
        return BankAccount.objects.order_by('-current_balance')

    def get_bank_account_by_id(self, bank_id):
        return BankAccount.objects.get(id=bank_id)
