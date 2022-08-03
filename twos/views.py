from django.shortcuts import render
from django.views import generic
from .models import booking, menu, feedback


class bookingList(generic.ListView):
    model = booking
    queryset = booking.object.filter(status=1)
    template_name = 'mybookings.html'
    paginate_by = 3


class menuList(generic.ListView):
    model = menu
    queryset = menu.objects.filter(status=1).order_by('-created_on')
    template_name = 'menu.html'
    paginate_by = 2

class feedbackList(generic.ListView):
    model = feedback
    queryset = feedback.objects.filter(status=1).order_by('-created_on')
    template_name = 'feedback.html'
    paginate_by = 4