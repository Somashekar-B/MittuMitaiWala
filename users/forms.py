from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from cart.models import Address
from store.models import Contact

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'address_line_1', 'address_line_2', 'landmark', 'city', 'pincode','phone' ]

class UserAddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'address_line_1', 'address_line_2', 'landmark', 'city', 'pincode','phone' ]

class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','content']
