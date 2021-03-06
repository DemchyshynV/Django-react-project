# Generated by Django 3.1.4 on 2021-01-14 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('order', '0007_auto_20210114_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='paymentMethod',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='payment_method',
            field=models.CharField(default='LiqPay', max_length=100),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='order_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='cart.cartitemsmodel'),
        ),
    ]
