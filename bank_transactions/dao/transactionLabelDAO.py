from bank_transactions.models import TransactionLabel


class TransactionLabelDAO:

    def create_label(self, label_name: str, label_details=None) -> TransactionLabel:
        return TransactionLabel.objects.create(label_name=label_name, label_details=label_details)

    def get_or_create_label(self, label_name: str) -> TransactionLabel:
        try:
            return TransactionLabel.objects.get(label_name=label_name)
        except TransactionLabel.DoesNotExist:
            return self.create_label(label_name)

    def get_transactions_for_label(self, label_name: str) -> TransactionLabel:
        label = TransactionLabel.objects.get(label_name=label_name)
        return label.transaction_set.all().order_by('-transaction_date')

    def get_all_labels(self):
        return TransactionLabel.objects.order_by('label_name')

    def get_label_info_by_name(self, label_name: str) -> TransactionLabel:
        return TransactionLabel.objects.get(label_name=label_name)
