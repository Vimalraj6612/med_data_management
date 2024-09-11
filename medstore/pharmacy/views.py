from django.shortcuts import render
# from .models import Dealer
# from .models import Employee
# from .models import Customer
# from .models import Medicine
# from .models import Purchase
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request,'pharmacy/index.html')
