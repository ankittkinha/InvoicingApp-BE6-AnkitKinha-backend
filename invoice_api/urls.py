from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"), 
    path("login/", LoginView.as_view(), name="login"),
    path("invoices/", InvoiceView.as_view(), name="all-invoices"),
    path("invoices/new/", InvoiceView.as_view(), name="post-invoice"),
    path("invoices/<int:id>/", SpecificInvoiceView.as_view(), name="specific-invoice"),
    path("invoices/<int:id>/items/", AddItem.as_view(), name="add-item"),
]   