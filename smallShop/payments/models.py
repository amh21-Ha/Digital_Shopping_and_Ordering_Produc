from django.db import models
from orders.models import Order
import django.utils.timezone
from datetime import datetime, timezone

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.IntegerField(default=int(datetime(2024, 7, 11, 13, 37, 58, 172792, tzinfo=timezone.utc).timestamp()))
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])

    def __str__(self):
        return f"Payment of {self.amount} for Order {self.order.id}"
