"""
registering models to admin panel
"""
from django.contrib import admin
from .models import Booking, Feedback


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Shows the bookings tab in the admin panel
    """
    model = Booking
    list_display = (
        'first_name', 'email_address',
        'reservation_time', 'booking_date',
        )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Shows the feedback tab in the admin panel
    """
    model = Feedback
    list_display = ('first_name', 'comment')
    actions = ["approve_feedback"]

    def approve_feedback(self, queryset):
        """
        Allows admins to set a booking to approved
        """
        queryset.update(approved=True)
