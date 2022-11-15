from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackList.as_view(), name="home"),
    path('bookings', views.CreateBookingView.as_view(), name="bookings"),
    path('bookingupdate/<int:pk>/', views.UpdateBookings.as_view(), name='bookingupdate')
]
