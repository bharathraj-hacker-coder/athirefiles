# Generated by Django 4.0.1 on 2022-01-11 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LogIn', '0002_rename_signin_credentials_login_credentials'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login_credentials',
            new_name='signin_credentials',
        ),
    ]
