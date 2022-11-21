from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackList.as_view(), name="home"),
    path('bookings', views.CreateBookingView.as_view(), name="bookings"),
    path('viewbookings', views.ViewBookings.as_view(), name='viewbookings'),
    path('booking_edit/<booking_id>', views.booking_edit_view, name='update'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete'),
    path('feedback', views.CreateFeedbackView.as_view(), name="feedback"),
]
