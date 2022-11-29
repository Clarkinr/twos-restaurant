# TWOs restaurant
This project consists of a website and booking system for a restaurant called Twos. 

For this project I have used Github to store the project, GitPod as the editor and Heroku for project deployment

A live link to the active site can be found [here](https://twos-restaurant.herokuapp.com/)

## Reasons for creation
I previously worked in the service industry and am interested in how online booking has become so popular in the past few years.
A booking system can be used for a multitude of businesses and seemed like a useful project to undertake 

## Technology used:
- Django
- Python
- github
- gitpod
- heroku
- cloudinary
- Postgres - later changed to elephant
- Elephant

## Wireframes 

- Below are the wireframes created to base the site design on. The aim was to keep a lot of white space and use individual pages for CRUD functionality. 


![home-wireframe](/static/images/wireframes/homepage.PNG)
![sign-up-wireframe](/static/images/wireframes/sign-up.PNG)
![sign-in-wireframe](/static/images/wireframes/sign-in.PNG)
![sign-out-wireframe](/static/images/wireframes/sign-out.PNG)
![new-booking-wireframe](/static/images/wireframes/Booking-page.PNG)
![current-booking-wireframe](/static/images/wireframes/current-bookings.PNG)


## User Stories
- Below are samples of the created user stories, a full list of completed user stories can be found in the github projects tab for this repository


![sample-user-stories](/static/images/sample-user-stories.PNG)

## Models
### CRUD functionality
- The relationship entity diagrams and crud tables for the models used can be seen in the image below. 

![CRUD-relationship-diagram](/static/images/models-crud-tables.PNG)

### Choices
- I needed to create choices for the time and number of people attending which can be seen as a drop down in the 
BookingFrom


![choices](/static/images/choices-model.PNG)

### Booking Model

- Below is an image of the booking model this model is used to create the booking form which allows users or administrators to 
create a new booking to be approved by the administrators.



![bookingmodel](/static/images/booking-model.PNG)

### Feedback Model
- Below is the Feedback model, the feedback model is used to inform the booking form of which attrubutes need to be added to 
provide feedback to the restaurant. Once feedback is provided the administrator can choose to approve this feedback so that it 
appears on the index page of the site.



![feedback-model](/static/images/feedback-model.PNG)

## Views
### Class based views


- There are two class based views for each model (Booking and feedback). Both views are similar in structure so I will discuss 
only the ViewFeedback and CreateFeedbackView classes below(There is an image of both feedback and booking class based views for 
comparison)
- These class based views were each given their own unique url patterns so that the resulting pages could be added to the navbar 
for authenticated users. 
- The CreateFeedbackView class is used with the feedback.html file in order to display the feedback form for users to add their 
feedback. 
- The ViewFeedback class is used with the view_feedback.html file in order to allow users view their own previously submitted 
feedback (an admin can view all feed back submitted by any user)


![feedback-class-views](/static/images/feedback-class-views.PNG)
![booking-class-views](/static/images/booking-class-views.PNG)

### Feedback list view
- A final class based view was created for the feedback list. This view allows feedback submitted by users to be shown on the 
index page once it has been approved by an admin.

![feedback-list-class-views](/static/images/feedback-list-class.PNG)


### function based views
- There are two function based views provided for each of the booking and feedback models. The function based views are again 
similar and allow users to edit and delete bookings and feedback created previously, whether it has been approved or not. 
- These views retrieve the information previously added by the user via either the booking or feedback id and allow the user to 
update or delete the form they had previously provied.



![feedback-function-views](/static/images/feedback-function-views.PNG)
![booking-function-views](/static/images/booking-function-views.PNG)


## Features left to implement
- Limiting the number of seats available per day, currently a booking must be approved by an admin so can be managed that way. 
- Send automatic confirmation emails
- Allow admins post new menus from the admin panel (currently the menu is added as an image and has to be updated directly in the database )


## Code Validation 
- Code was checked for convnentional formatting using the pycodestyle function built into gitpod (this was formerly pep8).
- All pycodestyle errors were removed, there are two warnings in the views.py file shown below however, from some google searches
these appear to be common in django projects and I am unsure how to remove them. They do not affect the functionality of the code.
- All CSS was checked using the WS3 validator program (output can be seen below).



![WS3-validation](/static/images/W3c-css.PNG)
![code-warnings](/static/images/warning.PNG)


## Testing 
- The django tests.py file was used to create 5 view tests for booking, index, feedback, create feedback and update feedback
views
- For testing purposes the database was switched to sqlite3 in the settings.py file.
- The feedback view and booking view again are similar in nature so only one set was tested. All tests were checked for a 
response status code of 200 or success url. 
- The code for the tests can be seen below. 



![testcase-setup](/static/images/testcase.PNG)
![tests-booking-and-login](/static/images/test-booking-and-login.PNG)
![tests-feedback](/static/images/test-feedback.PNG)

## Deployment
- The following steps were taken to deploy the app to Heroku
1. Open the Heroku dashboard and select new and then create new app using the name twos-restaurant.
1. Open the Settings tab and add the Heroku/Python buildpack
1. Add the Elephant Database url to the Config Vars in the settings tab. 
1. Add the Database url to the my env.py file in gitpod
1. Add the Cloudinary_url to both env.py and to the Config Vars
1. Create a seceret key and add to both Config Vars and env.py
1. Update the settings.py file to reference the env.py file so it uses the correct Secret_Key and database.
1. Update the settings.py file to correctly reference cloudinary storage as the default media storage.
1. Add the TEMPLATES_DIR to settings.py file
1. in settings.py file change DEBUG value to True and update the ALLOWED_HOSTS with the heroku url and localhost.
1. Create the procfile. 
1. Link the repository from the heroku app dashboard
1. Change the settings.py file DEBUG Value to TREUE
1. Deploy the app using the Deply Branch and wait for heroku to finish the build.

## Credits
- The nav bar and footer along with the bootstrap links in the head section of the base.html file were adapted from the Code 
Institute "I think therefore I blog project"
