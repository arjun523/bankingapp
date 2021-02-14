from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('viewall',views.viewall,name="viewall"),
    path('transaction',views.transaction,name="transaction"),
    path('transfer',views.transfer,name="transfer"),
]
