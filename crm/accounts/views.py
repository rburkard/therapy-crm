from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from . forms import OrderForm, CustomerForm
from .filters import OrderFilter

#-------------------(DETAIL/LIST VIEWS) -------------------

def dashBoard(request):
	orders = Order.objects.all().order_by('-status')[0:5]
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = Order.objects.all().count()
	open_orders = Order.objects.filter(status='Open').count()
	paid_orders = Order.objects.filter(status='Paid').count()
	overdue_orders = Order.objects.filter(status='Overdue').count()



	context = {'customers':customers, 'orders':orders,
	'total_customers':total_customers,'total_orders':total_orders, 
	'open_orders':open_orders, 'paid_orders':paid_orders, 'overdue_orders':overdue_orders}
	return render(request, 'accounts/dashBoard.html', context)

def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	total_orders = orders.count()



	orderFilter = OrderFilter(request.GET, queryset=orders) 
	orders = orderFilter.qs

	context = {'customer':customer, 'orders':orders, 'total_orders':total_orders,
	'filter':orderFilter}
	return render(request, 'accounts/customer.html', context)


#-------------------(CREATE VIEWS) -------------------

def createOrder(request):
	action = 'create'
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/order_form.html', context)

def createCustomer(request):
	action = 'create'
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/customer_form.html', context)

#-------------------(UPDATE VIEWS) -------------------

def updateOrder(request, pk):
	action = 'update'
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/customer/' + str(order.customer.id))

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/order_form.html', context)

def updateCustomer(request, pk):
	action = 'update'
	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('/customer/' + str(customer.id))

	context =  {'action':action, 'form':form}
	return render(request, 'accounts/customer_form.html', context)

#-------------------(DELETE VIEWS) -------------------

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		customer_id = order.customer.id
		customer_url = '/customer/' + str(customer_id)
		order.delete()
		return redirect('/')
		
	return render(request, 'accounts/delete_item.html', {'item':order})


def deleteCustomer(request, pk):
	customer = Customer.objects.get(id=pk)
	if request.method == 'POST':
		customer_id = customer.id
		customer_url = '/customer/' + str(customer_id)
		customer.delete()
		return redirect('/')
		
	return render(request, 'accounts/delete_item.html', {'item':customer})
