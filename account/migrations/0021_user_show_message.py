# Generated by Django 3.0.5 on 2020-09-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_remove_user_show_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_message',
            field=models.BooleanField(default=False),
        ),
    ]
