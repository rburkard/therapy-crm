# Generated by Django 3.1.5 on 2021-01-30 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='end_time',
            new_name='finish_time',
        ),
    ]
