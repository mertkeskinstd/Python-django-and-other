# Generated by Django 4.2.6 on 2023-11-05 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tweetapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tweet",
            name="nickname",
        ),
        migrations.AddField(
            model_name="tweet",
            name="username",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
