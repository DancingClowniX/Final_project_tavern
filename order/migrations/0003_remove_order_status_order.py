# Generated by Django 5.0.6 on 2024-08-04 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_quantity_remove_order_taking_summa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status_order',
        ),
    ]