# Generated by Django 4.1.7 on 2023-04-14 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_last_login_user_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
    ]