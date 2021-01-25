from django.db import models

# Create your models here.

class Customer(models.Model):
	GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
		('X', 'Not disclosed')
    ]

	gender = models.CharField(max_length=2, choices=GENDER_CHOICES,default='F', null=True)
	salutation = models.CharField(max_length=200, null=True)
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True, default='')
	date_of_birth = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.first_name

	@property
	def orders(self):
		order_count = self.order_set.all().count()
		return str(order_count)



class Order(models.Model):
	STATUS = (
			('Open', 'Open'),
			('Paid', 'Paid'),
			('Overdue', 'Overdue'),
			) 

	customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)
	description1 = models.TextField(null=True)
	description2 = models.TextField(null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.customer)


