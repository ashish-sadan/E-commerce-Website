# Generated by Django 5.0.4 on 2024-05-26 04:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vedaitapp", "0007_rename_user_users_alter_customer_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Users",
            new_name="User",
        ),
    ]
