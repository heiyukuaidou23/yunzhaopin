# Generated by Django 2.2.28 on 2023-09-18 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_seekerprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seeker_profile', to='app1.JobSeeker'),
        ),
    ]