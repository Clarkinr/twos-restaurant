from django.shortcuts import render
from django.views import generic
from .models import booking, feedback


class BookingList(generic.ListView):
    model = booking
    queryset = booking.objects.filter(Status=1).order_by("-reservation_made")
    template_name = 'bookings.html'


class FeedbackList(generic.ListView):
    model = feedback
    queryset = feedback.objects.filter(Status=1).order_by("-feedback_made")
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        return feedback.objects.filter(Status=1)
