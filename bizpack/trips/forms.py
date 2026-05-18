from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'departure_date', 'return_date', 'climate', 'meeting_type', 'notes']
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. Black tie dinner on Thursday, outdoor factory visit on Friday'}),
        }
