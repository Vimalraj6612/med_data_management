from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),

    path('dealerform/', views.dealerform, name="dealerform"),
    path('dealerforminsert/', views.dealerforminsert, name="dealerforminsert"),
    path('dealerformupdate(?P<foo>[0-9]+)/', views.dealerformupdate, name="dealerformupdate"),
    path('dealerformview(?P<foo>[0-9]+)/', views.dealerformview, name="dealerformview"),
    path('dealerformdelete(?P<foo>[0-9]+)/', views.dealerformdelete, name="dealerformdelete"),
    path('dealertable/', views.dealertable, name='dealertable'),

    path('medform/', views.medform, name="medform"),
    path('medforminsert/', views.medforminsert, name="medforminsert"),
    path('medformupdate(?P<foo>[0-9]+)/', views.medformupdate, name="medformupdate"),
    path('medformview(?P<foo>[0-9]+)/', views.medformview, name="medformview"),
    path('medformdelete(?P<foo>[0-9]+)/', views.medformdelete, name="medformdelete"),
    path('medtable/', views.medtable, name='medtable'),

    path('empform/', views.empform, name="empform"),
    path('empforminsert/', views.empforminsert, name="empforminsert"),
    path('empformupdate(?P<foo>[0-9]+)/', views.empformupdate, name="empformupdate"),
    path('empformview(?P<foo>[0-9]+)/', views.empformview, name="empformview"),
    path('empformdelete(?P<foo>[0-9]+)/', views.empformdelete, name="empformdelete"),
    path('emptable/', views.emptable, name='emptable'),

    path('custform/', views.custform, name="custform"),
    path('custforminsert/', views.custforminsert, name="custforminsert"),
    path('custformupdate(?P<foo>[0-9]+)/', views.custformupdate, name="custformupdate"),
    path('custformview(?P<foo>[0-9]+)/', views.custformview, name="custformview"),
    path('custformdelete(?P<foo>[0-9]+)/', views.custformdelete, name="custformdelete"),
    path('custtable/', views.custtable, name='custtable'),

    path('purchaseform/', views.purchaseform, name="purchaseform"),
    path('purchaseforminsert/', views.purchaseforminsert, name="puchaseforminsert"),
    path('purchaseformupdate(?P<foo>[0-9]+)/', views.purchaseformupdate, name="purchaseformupdate"),
    path('purchaseformview(?P<foo>[0-9]+)/', views.purchaseformview, name="purchaseformview"),
    path('purchaseformdelete(?P<foo>[0-9]+)/', views.purchaseformdelete, name="purchaseformdelete"),
    path('purchasetable/', views.purchasetable, name='purchasetable')

]