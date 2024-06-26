# Generated by Django 4.2 on 2024-04-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_hashtag_product_hashtags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='products.hashtag'),
        ),
    ]
