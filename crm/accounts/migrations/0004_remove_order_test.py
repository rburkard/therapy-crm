# Generated by Django 3.1.5 on 2021-01-30 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210130_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='test',
        ),
    ]