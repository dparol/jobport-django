# Generated by Django 4.1.5 on 2023-01-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]