"""
views to be generated for users
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormView
from .models import Booking, Feedback
from .forms import BookingForm, FeedbackForm


class CreateBookingView(FormView):
    '''view which allows users to create a new booking'''
    template_name = 'bookings.html'
    form_class = BookingForm
    success_url = 'booking_requested.html'

    def post(self, request):
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

        return render(request, 'booking_requested.html')


class ViewBookings(generic.DetailView):
    """View which allows users see previously created bookings"""

    template_name = 'view_bookings.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)

            return render(request, 'view_bookings.html', {
                    'bookings': bookings
                })
        else:
            return redirect('account_login')


def booking_edit_view(request, booking_id):
    """
    View which allows users to edi bookings previously created
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(data=request.POST, instance=booking)
        if form.is_valid():
            form.save()
        return redirect('/')

    form = BookingForm(instance=booking)

    return render(request, 'booking_edit.html', {'form': form})


def delete_booking(request, booking_id):
    """
    View generated after user chooses to delete a booking
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return render(request, 'view_bookings.html')


class CreateFeedbackView(FormView):
    '''view for the feedback Form'''
    template_name = 'feedback.html'
    form_class = FeedbackForm
    success_url = 'feedback_submitted.html'

    def post(self, request):
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()

        return render(request, 'feedback_submitted.html')


class ViewFeedback(generic.DetailView):
    """Allows users to view Feedback previously made """

    template_name = 'view_feedback.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            feedbacks = Feedback.objects.filter(user=request.user)

            return render(request, 'view_feedback.html', {
                    'feedbacks': feedbacks
                })
        else:
            return redirect('account_login')


def feedback_edit_view(request, feedback_id):
    """View which allows users see feedback they have made"""
    feedback = get_object_or_404(Feedback, id=feedback_id)

    if request.method == 'POST':
        form = FeedbackForm(data=request.POST, instance=feedback)
        if form.is_valid():
            form.save()
        return redirect('/')

    form = FeedbackForm(instance=feedback)

    return render(request, 'feedback_edit.html', {'form': form})


def delete_feedback(request, feedback_id):
    """
    View which allows users to delete feedback they have made
    and returns them to the view feedback page
    """
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.delete()
    return render(request, 'view_feedback.html')


class FeedbackList(generic.ListView):
    '''view to show the approved feed back listed on the index page'''
    model = Feedback
    queryset = Feedback.objects.filter(Status=1).order_by("-feedback_made")
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        return Feedback.objects.filter(Status=1)
