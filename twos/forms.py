import datetime
from .models import booking
from django import forms
from django.forms import ModelForm, Form


class BookingForm(ModelForm):
    
    first_name = forms.CharField(
        label='First Name',
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        label='Last Name',
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'Second Name'}),
    )

    email_address = forms.EmailField(
        label='Email',
        required = True,
        widget=forms.TextInput(attrs={'placeholder': 'email'}),
    )

    booking_date = forms.DateField(
        label='date in format YYYY-MM-DD',
        required=True,
        widget=forms.DateInput(attrs={'placeholder': '2022-08-10'})
    )
    

    class Meta:
        model = booking
        fields = '__all__'
        exclude = ('user', 'Status',)
