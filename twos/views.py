from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormView
from .models import Booking, Feedback
from .forms import BookingForm, FeedbackForm


class CreateBookingView(FormView):
    '''view for the bookings Form'''
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


class ViewBookings(generic.DetailView):

    template_name = 'viewbookings.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)

            return render(request, 'viewbookings.html', {
                    'bookings': bookings
                })
        else:
            return redirect('account_login')


def booking_edit_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            form.save()
        return redirect('/')

    form = BookingForm(instance=booking)

    return render(request, 'booking_edit.html', {'form': form})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return render(request, 'viewbookings.html')


class CreateFeedbackView(FormView):
    '''view for the feedback Form'''
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = 'feedbacksubmitted.html'

    def post(self, request):
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()

        return render(request, 'feedbacksubmitted.html')


class FeedbackList(generic.ListView):
    '''view to show the approved feed back listed on the index page'''
    model = Feedback
    queryset = Feedback.objects.filter(Status=1).order_by("-feedback_made")
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        return Feedback.objects.filter(Status=1)
