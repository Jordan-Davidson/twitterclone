from django.db import models
from tweet.models import Tweet
from twitterUser.models import TwitterUser

# Create your models here.
class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE,default=None)
    reciver = models.ForeignKey(TwitterUser,on_delete=models.CASCADE,null=True, related_name="notification_sender")
    viewed = models.DateTimeField(default=None,null=True,blank=True)