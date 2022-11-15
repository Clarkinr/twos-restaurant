from django.contrib import admin
from .models import Booking, Feedback


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    model = Booking
    list_display = (
        'first_name', 'email_address',
        'reservation_time', 'booking_date'
        )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ('first_name', 'comment')
    actions = ["approve_feedback"]

    def approve_feedback(self, request, queryset):
        queryset.update(approved=True)
