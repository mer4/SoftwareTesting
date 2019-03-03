# Generated by Django 2.1.7 on 2019-03-03 22:39

import SpeechToText.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SpeechToText', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Transcript', models.TextField()),
                ('UploadedDate', models.DateField(default=django.utils.timezone.now)),
                ('Content', models.FileField(upload_to=SpeechToText.models.scramble_uploaded_filename, verbose_name='UploadedFiles')),
            ],
        ),
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='Type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SpeechToText.FileType'),
        ),
        migrations.AddField(
            model_name='file',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]