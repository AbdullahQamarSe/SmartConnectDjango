# Generated by Django 4.1.7 on 2023-05-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0012_alter_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=122)),
                ('CategoryDes', models.CharField(max_length=122)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
