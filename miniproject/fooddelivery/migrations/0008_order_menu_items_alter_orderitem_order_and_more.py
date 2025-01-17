# Generated by Django 5.1.3 on 2024-11-21 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddelivery', '0007_remove_order_total_amount_alter_orderitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='menu_items',
            field=models.ManyToManyField(related_name='orders', through='fooddelivery.OrderItem', to='fooddelivery.menuitem'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='fooddelivery.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
