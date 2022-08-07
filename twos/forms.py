from .models import feedback
from django import forms


class FeedbackForm(forms.ModelForm):
       
    class Meta:
        model = feedback
        fields = '__all__'
        exclude = ('first_name', 'second_name',)
        comment = forms.CharField(
            label = "feedback",
            required=True,
        )