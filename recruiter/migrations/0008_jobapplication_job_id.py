# Generated by Django 4.1.5 on 2023-01-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0007_remove_jobapplication_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='job_id',
            field=models.IntegerField(null=True),
        ),
    ]