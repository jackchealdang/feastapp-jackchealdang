# Generated by Django 3.0.4 on 2020-03-07 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_songs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Songs',
        ),
    ]