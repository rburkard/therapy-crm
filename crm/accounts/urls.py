from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashBoard, name="dashboard"),
    path('customer/<str:pk>/', views.customer, name="customer"),

    #------------ (CREATE URLS) ------------
    path('create_order/', views.createOrder, name="create_order"),
    path('create_order_per_customer/<str:pk>/', views.createOrderPerCustomer, name="create_order_per_customer"),
    path('create_customer/', views.createCustomer, name="create_customer"),
   
    #------------ (UPDATE URLS) ------------
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),


    #------------ (UPDATE URLS) ------------
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"),

]
