# Generated by Django 5.2.2 on 2025-06-21 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_user_temp_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="temp_username",
        ),
    ]
