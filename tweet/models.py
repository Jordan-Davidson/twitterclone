from django.db import models
from django.utils import timezone
from twitterUser.models import TwitterUser

# Create your models here.
class Tweet(models.Model):
    username = models.ForeignKey(TwitterUser,on_delete=models.CASCADE,related_name="tweets")
    body = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.body