from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, total=0, status='Pending')
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product, price=product.price)
    order_item.quantity += 1
    order_item.save()
    order.total += product.price
    order.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, status='Pending').first()
    return render(request, 'orders/cart.html', {'order': order})

@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, status='Pending').first()
    if order:
        # Assume payment processing is done here
        order.status = 'Completed'
        order.save()
        return redirect('order_confirmation', order_id=order.id)
    return redirect('index')
