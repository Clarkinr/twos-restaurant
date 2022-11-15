from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormView, BaseUpdateView
from .models import Booking, Feedback
from .forms import BookingForm

'''view for the bookings Form'''


class CreateBookingView(FormView):
    template_name = 'bookings.html'
    form_class = BookingForm
    success_url = 'bookingrequested.html'

    def post(self, request):
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

        return render(request, 'bookingrequested.html')


class UpdateBookings(generic.UpdateView):
    
    model = Booking
    template_name = 'bookingupdate.html'
    form_class = BookingForm
    success_url = 'bookingrequested.html'
    

    def post(self, request):
        form = Booking.object.get(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user.id
            booking.save()

        return render(request, 'bookingrequested.html')


'''view to show the approved feed back listed on the index page'''


class FeedbackList(generic.ListView):
    model = Feedback
    queryset = Feedback.objects.filter(Status=1).order_by("-feedback_made")
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        return Feedback.objects.filter(Status=1)
