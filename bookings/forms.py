from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking
from datetime import date

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered')
        return email

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service_type', 'booking_date', 'booking_time', 'notes']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any special requests?'}),
        }
    
    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date < date.today():
            raise forms.ValidationError('Booking date cannot be in the past')
        return booking_date