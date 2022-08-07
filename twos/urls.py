from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackList.as_view(), name="home"),
    path('bookings', views.BookingView.as_view(), name="bookings")
]
