from django.urls import path
from views import RequestEvent


urlpatterns = [
    path('hello_world', RequestEvent.as_view()),
]
