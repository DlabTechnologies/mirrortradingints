# Generated by Django 3.0.5 on 2020-09-17 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_user_show_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='show_message',
        ),
    ]
