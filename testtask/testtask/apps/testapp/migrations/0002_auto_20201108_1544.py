# Generated by Django 3.0.7 on 2020-11-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]
