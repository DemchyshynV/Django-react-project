# Generated by Django 3.1.4 on 2020-12-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Shirts', 'Shirts'), ('Pants', 'Pants')], default='Shirts', max_length=50)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('price', models.FloatField()),
                ('countInStock', models.IntegerField()),
                ('brand', models.CharField(choices=[('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Lacoste', 'Lacoste'), ('Puma', 'Puma')], default='Adidas', max_length=62)),
                ('rating', models.FloatField()),
                ('numReviews', models.IntegerField()),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]