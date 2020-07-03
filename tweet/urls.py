  
from django.urls import path
from tweet import views


urlpatterns = [
    path("" , views.maintweets, name='homepage'),
    path("<str:username>/<int:id>/", views.singletweet),
    path("<str:username>/", views.profiletweets, name='profile'),
    path("<str:username>/NEW", views.MakeTweet),
]