# Generated by Django 4.1.4 on 2022-12-21 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('address_line_1', models.CharField(blank=True, max_length=50)),
                ('address_line_2', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('pin_code', models.IntegerField()),
                ('highest_qualification', models.IntegerField()),
                ('year_of_passout', models.IntegerField()),
                ('degree_college', models.CharField(blank=True, max_length=50)),
                ('cgpa', models.IntegerField()),
                ('degree_passout', models.IntegerField()),
                ('plus_two_school', models.CharField(blank=True, max_length=50)),
                ('plus_two_persentage', models.IntegerField()),
                ('plus_two_passout', models.IntegerField()),
                ('tenth_school', models.CharField(blank=True, max_length=50)),
                ('tenth_year', models.IntegerField()),
                ('tenth_persentage', models.IntegerField()),
                ('currentRole', models.CharField(blank=True, max_length=50)),
                ('currentCTC', models.IntegerField()),
                ('ECTC', models.IntegerField()),
                ('total_experiance', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('NoticePeriod', models.CharField(blank=True, max_length=50)),
                ('CurrentLocation', models.CharField(blank=True, max_length=50)),
                ('PreferredLocations', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.account')),
            ],
        ),
    ]
