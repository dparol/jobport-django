# Generated by Django 4.1.5 on 2023-01-12 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0008_jobapplication_job_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='job_id',
        ),
    ]
