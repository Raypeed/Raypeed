from django.urls import path
from . import views

urlpatterns =[
    path('', views.PaymentAPIView, name = 'Pay'),
]