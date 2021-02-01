# Generated by Django 3.1.5 on 2021-01-31 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Paid', 'Paid'), ('Overdue', 'Overdue')], max_length=200, null=True),
        ),
    ]