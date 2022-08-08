from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from .models import booking, feedback
from .forms import BookingForm

'''view for the bookings Form'''


class BookingView(FormView):
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


'''view to show the approved feed back listed on the index page'''


class FeedbackList(generic.ListView):
    model = feedback
    queryset = feedback.objects.filter(Status=1).order_by("-feedback_made")
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        return feedback.objects.filter(Status=1)
