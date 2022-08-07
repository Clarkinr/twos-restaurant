import datetime
from .models import booking
from django import forms
from django.forms import ModelForm, Form

class BookingForm(ModelForm):
    
    first_name = forms.CharField(
        label='First Name',
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'first_name'}),
    )

    last_name = forms.CharField(
        label='Last Name',
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'second_name'}),
    )

    email_address = forms.EmailField(
        label='Email',
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'second_name'}),
    )

    class Meta:
        model = booking
        fields = '__all__'
        exclude= ('user', 'Status',)