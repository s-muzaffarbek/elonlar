# Generated by Django 4.2 on 2023-05-02 19:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=datetime.datetime(2023, 5, 2, 19, 33, 46, 393447, tzinfo=datetime.timezone.utc), on_delete=django.db.models.deletion.CASCADE, to='product.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='phones',
            field=models.IntegerField(max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]