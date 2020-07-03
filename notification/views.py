from django.shortcuts import render
from notification.models import Notification
from twitterUser.models import TwitterUser
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/welcome/")
def read_notification(request,username):
    all_notifications = Notification.objects.filter(reciver__username=request.user.username)
    tweetlist = []
    pageuser = TwitterUser.objects.filter(username=username).first()
    tweetlist = sorted(tweetlist, key=lambda l: (l.time), reverse=True)
    for notification in all_notifications:
        if not notification.viewed:
            tweetlist.append(notification.tweet)
        notification.viewed = timezone.now()
        notification.save()
    count = len(tweetlist)
    return render(request, "defaulthome.html",{"pageuser":pageuser,"tweets":tweetlist,'count':count})