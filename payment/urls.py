from django.urls import path
from . import views


urlpatterns = [
    path('payment_success', views.payment_success, name='payment-success'),
    path('checkout', views.checkout, name='checkout'),
    path('billing_info', views.billing_info, name='billing-info'),
    path('process_order/', views.process_order, name='process-order'),
    path('shipped_dash/', views.shipped_dash, name='shipped-dash'),
    path('not_shipped_dash/', views.not_shipped_dash, name='not-shipped-dash'),
    path('orders/<int:pk>', views.orders, name='orders'),

]
