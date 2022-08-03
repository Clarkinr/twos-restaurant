from . import views
from django.urls import path


urlpatterns = [
    path('',views.menuList.as_view(), name="home")
]