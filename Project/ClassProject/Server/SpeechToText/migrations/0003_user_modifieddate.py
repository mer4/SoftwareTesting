# Generated by Django 2.1.7 on 2019-02-28 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SpeechToText', '0002_user_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ModifiedDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
