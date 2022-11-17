import datetime
from django import forms
from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):

    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Second Name'}),
    )

    email_address = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'email'}),
    )

    booking_date = forms.DateField(
        initial=datetime.date.today,
        widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ('user', 'Status',)
