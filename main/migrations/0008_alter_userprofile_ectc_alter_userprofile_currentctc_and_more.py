# Generated by Django 4.1.5 on 2023-01-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_userprofile_cgpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ECTC',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='currentCTC',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tenth_persentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tenth_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='total_experiance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
