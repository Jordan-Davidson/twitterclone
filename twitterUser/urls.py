from django.urls import path
from twitterUser import views

urlpatterns = [
    path('follow/<str:username>/<str:username2>', views.follow),
    path('unfollow/<str:username>/<str:username2>', views.unfollow)
]