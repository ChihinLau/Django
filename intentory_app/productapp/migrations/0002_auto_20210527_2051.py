# Generated by Django 3.2.3 on 2021-05-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
