# Generated by Django 4.1.7 on 2023-04-11 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_password1_user_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_confirmation',
        ),
    ]