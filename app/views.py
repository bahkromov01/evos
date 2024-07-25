from django.shortcuts import render
from django.db.models import Sum, Min, Max, Count, Avg

from app.models import Product, Customer, Order

# Create your views here.


total_count = Product.objects.count()


average_value = Product.objects.aggregate(avg=Avg('name'))['avg']


max_value = Customer.objects.aggregate(max=Max('name'))['max']

min_value = Product.objects.aggregate(min=Min('name'))['min']

total_sum = Order.objects.aggregate(sum=Sum('quantity'))['sum']

results = Customer.objects.filter(some_condition=True).aggregate(
    total_count=Count('id'),
    total_sum=Sum('name')
)


top_categories = Product.objects.values('').annotate(sum_price=Sum('')).order_by('-sum_price')[:5]


from django.db.models import Sum

# Calculate the total revenue from orders placed in 2022
total_revenue_2022 = Order.objects.filter(placed_at__year=2022).aggregate(total=Sum('total_cost'))['total']


products_with_order_counts = Product.objects.annotate(order_count=Count('order__id'))



