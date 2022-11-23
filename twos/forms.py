"""
Forms to be used with models
"""
import datetime
from django import forms
from django.forms import ModelForm
from .models import Booking, Feedback


class BookingForm(ModelForm):
    """
    provides information shown to user when creating a booking
    and generates the form
    """

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
        """
        provides the BookingForm with the model to use and
        which fields to include/exclude
        """
        model = Booking
        fields = '__all__'
        exclude = ('user', 'Status',)


class FeedbackForm(ModelForm):
    """
    provides information shown to user when creating feedback
    and generates the form
    """

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

    comment = forms.CharField(
        label='Feedback',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'My experience was ...'})
        )

    class Meta:
        """
        provides the FeedbackForm with the model to use
        and which fields to include/exclude
        """
        model = Feedback
        fields = '__all__'
        exclude = ('user', 'Status', 'feedback_made', )
