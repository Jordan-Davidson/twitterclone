from django.shortcuts import render,reverse,HttpResponseRedirect
from twitterUser.models import TwitterUser
from notification.models import Notification
from tweet.models import Tweet
from tweet.forms import maketweet
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import re



# Create your views here.
@login_required(login_url='/welcome/')
def MakeTweet(request,username):
    if request.method == 'POST':
        Form = maketweet(request.POST)
        if Form.is_valid():
            data = Form.cleaned_data
            user = TwitterUser.objects.get(username=username)
            find_mentions = re.findall('@([\w]+)', data['body'])
            newtweet = Tweet.objects.create(
                body=data['body'],
                time=timezone.now(),
                username=user
            )
            if find_mentions:
                for mention in find_mentions:
                    for k in TwitterUser.objects.values('username'):
                        if mention == k['username'] :
                            reciver = TwitterUser.objects.get(username=mention)
                            Notification.objects.create(
                                tweet = newtweet,
                                reciver = reciver
                            )
        return HttpResponseRedirect(reverse('homepage'))
    form = maketweet()
    pageuser = TwitterUser.objects.filter(username=username).first()
    tweets = Tweet.objects.filter(username_id=pageuser.id).order_by('-time')
    all_notifications = Notification.objects.filter(reciver__username=request.user.username)
    count = len([n.viewed for n in all_notifications if not n.viewed])
    return render(request,'defaulthome.html', {'Form':form,'pageuser':pageuser,"tweets":tweets,"count":count})

def profiletweets(request,username):
    pageuser = TwitterUser.objects.filter(username=username).first()
    tweets = Tweet.objects.filter(username_id=pageuser.id).order_by('-time')
    all_notifications = Notification.objects.filter(reciver__username=request.user.username)
    count = len([n.viewed for n in all_notifications if not n.viewed])
    return render(request, 'defaulthome.html', {'pageuser':pageuser,"tweets":tweets,"count":count})

@login_required(login_url='/welcome/')
def maintweets(request):
    pageuser = TwitterUser.objects.filter(username=request.user.username).first()
    tweets = Tweet.objects.filter(username=pageuser)
    nyt = []
    for follower in pageuser.followers.all():
        nyt += Tweet.objects.filter(username=follower).order_by('-time')
    nyt = sorted(nyt, key=lambda l: (l.time),reverse=True)
    all_notifications = Notification.objects.filter(reciver__username=pageuser)
    count = len([n.viewed for n in all_notifications if not n.viewed])
    return render(request,'defaulthome.html',{"nyt":nyt,"tweets":tweets,"count":count})

def singletweet(request,username,id):
     tweet = Tweet.objects.filter(id=id)
     pageuser = tweet.first().username
     all_notifications = Notification.objects.filter(reciver__username=pageuser)
     count = len([n.viewed for n in all_notifications if not n.viewed])
     return render(request, 'defaulthome.html', {"tweets":tweet,"pageuser":pageuser,"count":count})