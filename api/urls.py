from django.urls import path
from .views import RequestEvent


urlpatterns = [
    path('', RequestEvent.as_view()),
]
