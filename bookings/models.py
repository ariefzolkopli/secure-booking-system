from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('consultation', 'Consultation'),
        ('maintenance', 'Maintenance'),
        ('repair', 'Repair'),
        ('installation', 'Installation'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.service_type} on {self.booking_date}"
    
    class Meta:
        ordering = ['-booking_date', '-booking_time']

class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('login_success', 'Login Success'),
        ('login_failed', 'Login Failed'),
        ('logout', 'Logout'),
        ('booking_create', 'Booking Created'),
        ('booking_update', 'Booking Updated'),
        ('booking_delete', 'Booking Deleted'),
        ('admin_action', 'Admin Action'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.timestamp} - {self.user} - {self.action}"
    
    class Meta:
        ordering = ['-timestamp']