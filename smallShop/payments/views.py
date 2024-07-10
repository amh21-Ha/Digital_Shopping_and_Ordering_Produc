from django.shortcuts import render, get_object_or_404
from orders.models import Order
from .models import Payment

def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # Assume payment gateway integration here
    amount = order.total
    payment = Payment(order=order, amount=amount, status='Completed')
    payment.save()
    order.status = 'Completed'
    order.save()
    return render(request, 'payments/confirmation.html', {'order': order, 'payment': payment})
