"""
determines url patterns for the relevant views
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackList.as_view(), name="home"),
    path('bookings', views.CreateBookingView.as_view(), name="bookings"),
    path('view_bookings', views.ViewBookings.as_view(), name='view_bookings'),
    path('booking_edit/<booking_id>', views.booking_edit_view, name='b_edit'),
    path('delete_booking/<booking_id>', views.delete_booking, name='b_del'),
    path('feedback', views.CreateFeedbackView.as_view(), name="feedback"),
    path('view_feedback', views.ViewFeedback.as_view(), name='view_feedback'),
    path('feedback_edit/<feedback_id>', views.feedback_edit_view, name='f_ed'),
    path('delete_feedback/<feedback_id>', views.delete_feedback, name='del_f'),
]
