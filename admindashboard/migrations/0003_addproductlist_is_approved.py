# Generated by Django 2.2.4 on 2020-06-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0002_auto_20200613_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproductlist',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]