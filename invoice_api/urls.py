from django.urls import path
from .views import LoginView, RegisterView, InvoiceView, SpecificInvoiceView, AddItemView, NewInvoiceView


urlpatterns = [
    path("user/signup", RegisterView.as_view(), name="register"),
    path("user/login", LoginView.as_view(), name="login"),
    path("invoices", InvoiceView.as_view(), name="invoices"),
    path("invoices/new", NewInvoiceView.as_view(), name="new-invoice"),
    path("invoices/<int:id>", SpecificInvoiceView.as_view(), name="specific-invoice"),
    path("invoices/<int:invoice_id>/items", AddItemView.as_view(), name="add-item")
]