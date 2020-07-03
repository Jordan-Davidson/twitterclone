from django.urls import path
from authentication import views

urlpatterns = [
    path('welcome/', views.index, name='index'),
    path('login/', views.loginuser),
    path('logout/', views.logoutuser),
    path('signup/', views.signupuser),
]