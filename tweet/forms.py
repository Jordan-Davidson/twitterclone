from django import forms
from tweet.models import Tweet

class maketweet(forms.Form):
    body = forms.CharField(max_length=140,widget=forms.Textarea,label="Create a new Tweet here:(140 max)")