from django.shortcuts import render
from django.views import generic
from .models import booking, menu, feedback


class bookingList(generic.ListView):
    model = booking
    queryset = booking.objects.filter(Status=1)
    template_name = 'bookings.html'


class menuList(generic.ListView):
    model = menu
    template_name = 'index.html'
    paginate_by = 2


class feedbackList(generic.ListView):
    model = feedback
    template_name = 'index.html'
    paginate_by = 4