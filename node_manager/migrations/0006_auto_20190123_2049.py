# Generated by Django 2.1.4 on 2019-01-23 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('node_manager', '0005_auto_20190123_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='contact',
            new_name='contacts',
        ),
    ]
