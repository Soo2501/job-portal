# Generated by Django 4.2.3 on 2023-08-03 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-id']},
        ),
    ]
