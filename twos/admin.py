from django.contrib import admin
from .models import booking, feedback, menu

@admin.register(booking)
class bookingAdmin(admin.ModelAdmin):
    model = booking
    list_display = ('first_name', 'email_address', 'reservation_time', 'reservation_made')


@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    model = feedback
    list_display = ('first_name', 'comment')

@admin.register(menu)
class menuAdmin(admin.ModelAdmin):
    model = menu
    list_display = ('menu_image', 'menu_time')