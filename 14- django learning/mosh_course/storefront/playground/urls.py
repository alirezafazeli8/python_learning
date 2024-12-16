from . import views
from django.urls import path

# url configuration

urlpatterns = [path("helloworld/", views.say_hello)]
