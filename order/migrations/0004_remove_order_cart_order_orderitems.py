# Generated by Django 5.0.6 on 2024-08-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_order_status_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='order',
            name='orderItems',
            field=models.TextField(default=2, verbose_name='Корзина для заказа'),
            preserve_default=False,
        ),
    ]
