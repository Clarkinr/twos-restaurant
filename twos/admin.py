from django.contrib import admin
from .models import booking, feedback

@admin.register(booking)
class bookingAdmin(admin.ModelAdmin):
    model = booking
    list_display = ('first_name', 'email_address', 'reservation_time', 'booking_date')


@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    model = feedback
    list_display = ('first_name', 'comment')
    actions = ["approve_feedback"]

    def approve_feedback(self, request, queryset):
        queryset.update(approved=True)
