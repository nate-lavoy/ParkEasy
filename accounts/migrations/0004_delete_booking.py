# Generated by Django 5.1.6 on 2025-02-21 23:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Booking",
        ),
    ]
