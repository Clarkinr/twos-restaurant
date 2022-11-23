"""
Tests for views and basic CRUD functionality
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking, Feedback


class TestViews(TestCase):
    """
    Tests for the views.py file
    """

    def setUp(self):
        """
        Set up a test user, booking and feedback case
        """
        new_user = User.objects.create_user(
            username='barry',
            email='12time@time.com',
            password='Helpfulhint12'
        )

        Booking.objects.create(
            user=new_user,
            first_name='Barry',
            last_name='McDermot',
            email_address="12time@time.com",
            party_size='3',
            reservation_time='18:00',
            booking_date='2022-11-30'
        )

        Feedback.objects.create(
            user=new_user,
            first_name='Barry',
            last_name='McDermot',
            comment='lovely Dinner'
        )

    def login(self):
        """
        Logs in the previously created user
        """
        self.client.login(
            username='barry',
            password='Helpfulhint12'
        )

    def test_index_page(self):
        """
        test whether the index.html and base.html pages are loading correctly.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html', 'base.html')

    def test_booking_view(self):
        """
        test to determine that a user can view current bookings
        """
        response = self.client.get('/bookings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings.html', 'base.html')

    def test_feedback_view(self):
        """
        test whther a user can view previously made feedback
        """
        response = self.client.get('/feedback')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feedback.html', 'base.html')

    def test_create_feedback(self):
        """
        tests users ability to create feedback
        """
        self.login()
        response = self.client.post('/feedback')
        self.assertEqual(response.status_code, 200)

    def test_update_feedback(self):
        """
        tests a users ability to update feedback
        """
        feedback = Feedback.objects.get(first_name='Barry')
        response = self.client.get(f'/feedback_edit/{feedback.id}')
        self.assertEqual(response.status_code, 200)
