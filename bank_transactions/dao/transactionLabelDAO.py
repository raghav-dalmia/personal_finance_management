from bank_transactions.models import TransactionLabel


class TransactionLabelDAO:

    def create_label(self, label_name: str, label_details=None) -> TransactionLabel:
        return TransactionLabel.objects.create(label_name=label_name, label_details=label_details)

    def get_or_create_label(self, label_name: str) -> TransactionLabel:
        try:
            return TransactionLabel.objects.get(label_name=label_name)
        except TransactionLabel.DoesNotExist:
            return self.create_label(label_name)

    def get_all_labels(self) -> list:
        return TransactionLabel.objects.order_by('label_name')
