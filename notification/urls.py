from django.urls import path
from notification.views import read_notification

urlpatterns = [
    path('notifications/<str:username>',read_notification),
]