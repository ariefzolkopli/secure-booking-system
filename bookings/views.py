from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import RegisterForm, BookingForm
from .models import Booking, AuditLog
from .decorators import admin_required

def log_audit(request, action, details=''):
    AuditLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        action=action,
        ip_address=request.META.get('REMOTE_ADDR'),
        details=details
    )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            log_audit(request, 'login_success', 'New user registration')
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegisterForm()
    return render(request, 'bookings/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            log_audit(request, 'login_success', f'User {username} logged in')
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            log_audit(request, 'login_failed', f'Failed login attempt for {username}')
            messages.error(request, 'Invalid username or password')
    return render(request, 'bookings/login.html')

def user_logout(request):
    if request.user.is_authenticated:
        log_audit(request, 'logout', f'User {request.user.username} logged out')
    logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('home')

@login_required
def home(request):
    return render(request, 'bookings/home.html')

@login_required
def booking_list(request):
    if request.user.is_staff:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            log_audit(request, 'booking_create', f'Created booking #{booking.id} - {booking.service_type}')
            messages.success(request, 'Booking created successfully!')
            return redirect('booking_list')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form, 'title': 'Create Booking'})

@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if booking.user != request.user and not request.user.is_staff:
        messages.error(request, 'You can only edit your own bookings')
        return redirect('booking_list')
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            log_audit(request, 'booking_update', f'Updated booking #{booking.id}')
            messages.success(request, 'Booking updated successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/booking_form.html', {'form': form, 'title': 'Edit Booking'})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if booking.user != request.user and not request.user.is_staff:
        messages.error(request, 'You can only delete your own bookings')
        return redirect('booking_list')
    
    if request.method == 'POST':
        log_audit(request, 'booking_delete', f'Deleted booking #{booking.id}')
        booking.delete()
        messages.success(request, 'Booking deleted successfully!')
        return redirect('booking_list')
    return render(request, 'bookings/booking_confirm_delete.html', {'booking': booking})

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    return render(request, 'bookings/profile.html')

@admin_required
def audit_log(request):
    logs = AuditLog.objects.all()[:100]
    return render(request, 'bookings/audit_log.html', {'logs': logs})