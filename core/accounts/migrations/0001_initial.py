# Generated by Django 4.2.3 on 2023-08-01 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(default='xyz.jpg', upload_to='profile_images')),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('phone1', models.CharField(blank=True, max_length=10, null=True)),
                ('Address', models.CharField(max_length=120)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('starting_date', models.DateField(auto_now=True)),
                ('ending_date', models.DateField(auto_now=True)),
                ('institute_name', models.CharField(max_length=120)),
                ('image', models.FileField(upload_to='certificates')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField()),
                ('language', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('degree', models.CharField(max_length=120)),
                ('school_name', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now=True)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.FileField(upload_to='certificates')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctz_front', models.FileField(upload_to='documents')),
                ('ctz_back', models.FileField(upload_to='documents')),
                ('liscence', models.FileField(null=True, upload_to='documents')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
