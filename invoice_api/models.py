from django.db import models


class Invoices(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=100)
    date = models.DateField()
    
    
class Items(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE, related_name="items")
    desc = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()


class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
