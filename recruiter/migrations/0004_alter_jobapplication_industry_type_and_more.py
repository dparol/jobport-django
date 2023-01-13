# Generated by Django 4.1.5 on 2023-01-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_remove_jobapplication_salary_max_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='industry_type',
            field=models.CharField(choices=[('Business', 'Business'), ('it', 'IT/SOFTWARE'), ('banking', 'Banking'), ('education', 'Education'), ('telecommunication', 'telecommunication'), ('others', 'Others')], max_length=200),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_type',
            field=models.CharField(choices=[('permanent', 'permanent'), ('Temporary', 'Temporary'), ('intership', 'intership')], max_length=500),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='education',
            field=models.CharField(choices=[('bachlors', 'bachlors'), ('masters', 'masters'), ('phd', 'phd')], max_length=500),
        ),
    ]