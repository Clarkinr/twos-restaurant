from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Pending"), (1, "Approved"))

TIME_SLOTS = (
    ('18:00', '18:00'),
    ('20:30', '20:30'),
)

NUM_PEOPLE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)


class booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_book")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(null=True, blank=True)
    party_size = models.CharField(max_length=1, choices=NUM_PEOPLE, default='1')
    reservation_time = models.CharField(max_length=10, choices=TIME_SLOTS, default="18:00")
    reservation_made = models.DateTimeField(auto_now=True)
    Status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-reservation_made"]

    def __str__(self):
        return self.first_name


class feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_feedback")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    comment = models.TextField(max_length=350)
    feedback_made = models.DateTimeField(auto_now=True)
    Status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-feedback_made"]

    def __str__(self):
        return self.first_name


class menu(models.Model):
    menu_image = CloudinaryField('image', default='placeholder')
    menu_time = models.TextField()
    menu_made = models.DateTimeField(auto_now=True)
    Status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-menu_made"]

    def __str__(self):
        return self.menu_time
