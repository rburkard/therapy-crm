# Generated by Django 3.1.5 on 2021-01-31 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]