from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackList.as_view(), name="home"),
    path('menus/', views.MenuList.as_view(), name="menus")
]
