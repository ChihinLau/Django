# Generated by Django 3.2.3 on 2021-05-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_alter_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='default.jpg', upload_to='product_image'),
        ),
    ]
