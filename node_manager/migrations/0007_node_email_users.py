# Generated by Django 2.1.4 on 2019-02-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node_manager', '0006_auto_20190123_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='email_users',
            field=models.BooleanField(default=True),
        ),
    ]
