# Generated by Django 4.1.7 on 2023-04-06 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_password1_remove_user_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.CharField(default=12, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=12, max_length=12),
            preserve_default=False,
        ),
    ]
