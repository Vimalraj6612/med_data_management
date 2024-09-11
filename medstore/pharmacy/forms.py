from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['cust_id','f_name','l_name','ph_no','address','med_name','qty']