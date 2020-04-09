# Generated by Django 3.0.5 on 2020-04-08 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roulette', '0005_auto_20200402_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_meetings', to=settings.AUTH_USER_MODEL, to_field='uuid'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='time_ended',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Beendet'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tutor_meetings', to=settings.AUTH_USER_MODEL, to_field='uuid'),
        ),
    ]