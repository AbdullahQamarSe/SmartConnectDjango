# Generated by Django 4.1.7 on 2023-05-12 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_order_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_now',
            name='code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order_now',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order_now',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order_now',
            name='productName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='order_now',
            name='quantity',
            field=models.CharField(max_length=255),
        ),
    ]