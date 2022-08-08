# TWOs restaurant
This project is a website and basic booking system for a restaurant
## Reasons for creation
I previously worked in the service industry and am interested in how online booking has become so popular in the past few years.

## Technology used:
- Django
- Python
- github
- gitpod
- heroku
- cloudinary

## Models
### Choices
- firstly I needed to create choices for the time and number of people attending which can be seen as a drop down in the form. 
![choices](/static/images/choices-model.png)

### Booking Model
- Below is an image of the booking model this specifies all the information needed to add a booking to the admin panel and informs what will be used in the booking form.
![booking-model](../static/images/booking-model.png)

### Feedback Model
- The feedback Model is for the Admin panel only and is used for the feedback seen on the index.html page
![feedback-model](/static/images/feedback-model.png)

##Views
### Class based views
- Two custom class based views were created one for the booking form on the bookings page and one for the feedback shown on the index.html page
- These views were added to templates seen in the image below and extended a base.html file also seen below.
![views](/media/views.png)
![base-html](/static/images/base-html.png)


## Features left to implement
- Allow users modify and delete bookings
- Allow admins to specify a max number of seats available per day. 
- Send automatic confirmation emails
- Allow admins post new menus from the admin panel.
## Known bugs 
- The date field in the booking form will accept any input at present, if a non date input is added it will default to today, so if the admin sees today as the date to come in they should contact the user.

## Code Validation 
- Code was checked for convnentional formatting using the pycodestyle function built into gitpod (this was formerly pep8).
- All CSS was checked using the WS3 validator program (output can be seen below).
![WS3-validation](/static/images/W3c-css.png)


## Credits
- The nav bar and footer along with the bootstrap links in the head section of the base.html file were adapted from the Code Institute "I think therefore I blog project"
