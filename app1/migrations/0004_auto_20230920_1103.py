# Generated by Django 2.2.28 on 2023-09-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20230920_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='publishTime',
            field=models.DateField(auto_now_add=True),
        ),
    ]