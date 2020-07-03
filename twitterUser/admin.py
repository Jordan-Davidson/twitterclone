from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitterUser.models import TwitterUser
# Register your models here.


admin.site.register(TwitterUser, UserAdmin)