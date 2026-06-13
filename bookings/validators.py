# bookings/validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from datetime import date

def validate_service_type(value):
    allowed_services = ['Consultation', 'Maintenance', 'Repair', 'Installation', 'consultation', 'maintenance', 'repair', 'installation'] 
    if value not in allowed_services:
        raise ValidationError(_('%(value)s is not a valid service type'), params={'value': value})

def validate_booking_date(value):
    if value < date.today():
        raise ValidationError('Booking date cannot be in the past')

def validate_booking_time(value):
    from datetime import time
    if isinstance(value, str):
        hour, minute = map(int, value.split(':'))
        value = time(hour, minute)
    start_time = time(9, 0)
    end_time = time(17, 0)
    if value < start_time or value > end_time:
        raise ValidationError('Booking time must be between 9:00 AM and 5:00 PM')

def validate_phone_number(value):
    pattern = r'^(01[0-9]{8,9})$|^(\+601[0-9]{8,9})$'
    if value and not re.match(pattern, value):
        raise ValidationError('Enter a valid Malaysian phone number')

def validate_no_sql_injection(value):
    sql_patterns = ['SELECT', 'DROP', 'INSERT', 'DELETE', 'UPDATE', '--', ';', "' OR '1'='1"]
    value_upper = value.upper()
    for pattern in sql_patterns:
        if pattern in value_upper:
            raise ValidationError('Invalid characters in input')

# Password Complexity Validator
class ComplexityPasswordValidator:
    """Validate password complexity requirements"""
    
    def validate(self, password, user=None):
        errors = []
        
        if len(password) < 8:
            errors.append('Password must be at least 8 characters long')
        
        if not re.search(r'[A-Z]', password):
            errors.append('Password must contain at least one uppercase letter')
        
        if not re.search(r'[a-z]', password):
            errors.append('Password must contain at least one lowercase letter')
        
        if not re.search(r'[0-9]', password):
            errors.append('Password must contain at least one number')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append('Password must contain at least one special character')
        
        if errors:
            raise ValidationError(' '.join(errors))
    
    def get_help_text(self):
        return 'Password must contain at least 8 characters, including uppercase, lowercase, number, and special character.'