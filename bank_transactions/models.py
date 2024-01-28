from django.db import models, transaction
from bank_account.models import BankAccount
from django.core.validators import MinValueValidator


class TransactionLabel(models.Model):
    label_name = models.CharField(max_length=100, primary_key=True)  # RegexValidator for uppercase
    label_details = models.CharField(max_length=500, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    bank: BankAccount = models.ForeignKey(BankAccount, on_delete=models.CASCADE, null=False)
    transaction_details = models.CharField(max_length=500, null=True)
    transaction_date = models.DateTimeField()
    transaction_type = models.CharField(max_length=10, choices=(
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ))
    amount = models.DecimalField(max_digits=19, decimal_places=2, validators=[MinValueValidator(0)])
    label: TransactionLabel = models.ForeignKey(TransactionLabel, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if not getattr(self, '_updating_bank', False):
                self._updating_bank = True
                try:
                    if self.transaction_type == 'debit':
                        self.bank.current_balance -= self.amount
                    elif self.transaction_type == 'credit':
                        self.bank.current_balance += self.amount
                    self.bank.save()
                    super().save(*args, **kwargs)
                finally:
                    del self._updating_bank
