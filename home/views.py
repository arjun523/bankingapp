from django.shortcuts import render
from django.conf.urls.static import static
from .models import Customers,TransHistory
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def viewall(request):
    data = Customers.objects.all()
    return render(request,"viewall.html", {'data':data})

def transfer(request):
    if request.method == "POST":
        sender = Customers.objects.get(id=request.POST['s_id'])
        receiver = Customers.objects.get(id=request.POST['r_id'])
        transfer_amount = int(request.POST['amount'])
        print(sender.balance,receiver.balance,transfer_amount)
        if ((transfer_amount >0) and (sender.balance >= transfer_amount)):
            status = "Transaction Successful"
            receiver.balance = receiver.balance + transfer_amount
            sender.balance = sender.balance - transfer_amount
            print(sender.balance,receiver.balance)
            sender.save()
            receiver.save()
            messages.success(request,"Transaction Successful......Money Transfered!!!")
            
            obj = TransHistory()

            obj.s_name = sender.name
            obj.r_name = receiver.name
            obj.r_balance = receiver.balance
            obj.s_account = sender.account
            obj.r_account = receiver.account
            obj.amount_transfer = transfer_amount
            obj.status = status
            
            obj.save()
            
        else:
            status = "Transaction Failed"
            messages.error(request,"Transaction Failed....Try Again!!!")

            obj = TransHistory()

            obj.s_name = sender.name
            obj.r_name = receiver.name
            obj.r_balance = receiver.balance
            obj.s_account = sender.account
            obj.r_account = receiver.account
            obj.amount_transfer = transfer_amount
            obj.status = status
            
            obj.save()

    data = Customers.objects.all()
    return render(request,"transfer.html",{'data':data})

def transaction(request):
    data = TransHistory.objects.all()
    return render(request,"transaction.html",{'data':data})