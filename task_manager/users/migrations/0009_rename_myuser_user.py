# Generated by Django 4.1.7 on 2023-04-14 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_user_myuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='User',
        ),
    ]