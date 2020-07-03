# Generated by Django 3.0.6 on 2020-07-03 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notification', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='reciver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='tweet',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tweet.Tweet'),
        ),
    ]