# Generated by Django 3.0.4 on 2020-06-03 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addproductlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=100)),
                ('product_sku', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('supplier_username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='adminmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
