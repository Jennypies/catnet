# Generated by Django 2.1.4 on 2019-01-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node_manager', '0003_auto_20190106_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='node',
            name='last_contact',
            field=models.DateTimeField(editable=False, null=True, verbose_name='Last contact'),
        ),
        migrations.AddField(
            model_name='node',
            name='contact',
            field=models.ManyToManyField(to='node_manager.Contact'),
        ),
    ]
