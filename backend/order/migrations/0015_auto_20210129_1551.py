# Generated by Django 3.1.5 on 2021-01-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_cartitemsmodel_product'),
        ('order', '0014_auto_20210129_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='order_items',
            field=models.ManyToManyField(related_name='order', to='cart.CartItemsModel'),
        ),
    ]