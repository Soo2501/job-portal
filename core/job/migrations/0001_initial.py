# Generated by Django 4.2.3 on 2023-08-02 09:59

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
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('company', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('jtype', models.CharField(choices=[('fulltime', 'fulltime'), ('parttime', 'parttime'), ('contract', 'contract'), ('internship', 'internship')], max_length=120)),
                ('desc', models.TextField()),
                ('requirements', models.TextField()),
                ('wsite', models.CharField(max_length=120)),
                ('deadline', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
