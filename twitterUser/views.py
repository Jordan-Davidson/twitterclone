from django.shortcuts import render,reverse,HttpResponseRedirect
from twitterUser.models import TwitterUser

# Create your views here.
def follow(request,username,username2):
    user = TwitterUser.objects.filter(username=username).first()
    user2 = TwitterUser.objects.filter(username=username2).first()
    user2.followers.add(user)
    return HttpResponseRedirect(reverse('profile',args=(username,)))

def unfollow(request,username,username2):
    user = TwitterUser.objects.filter(username=username).first()
    user2 = TwitterUser.objects.filter(username=username2).first()
    user2.followers.remove(user)
    return HttpResponseRedirect(reverse('profile',args=(username,)))