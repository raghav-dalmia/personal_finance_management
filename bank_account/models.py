from django.db import models


class BankAccount(models.Model):
    id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=255)
    opening_balance = models.DecimalField(max_digits=19, decimal_places=2)
    current_balance = models.DecimalField(max_digits=19, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.current_balance = self.opening_balance
        super().save(*args, **kwargs)
