from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(default="",max_length=250)
    email = models.EmailField(max_length=250)
    account = models.CharField(max_length=50)
    balance = models.IntegerField(max_length=50)

class TransHistory(models.Model):
    s_name = models.CharField(default="",max_length=250)
    s_account = models.CharField(max_length=250)
    amount_transfer = models.IntegerField()
    r_name = models.CharField(default="",max_length=250)
    r_account = models.CharField(max_length=250)
    r_balance = models.IntegerField()
    status = models.CharField(default="",max_length=50)