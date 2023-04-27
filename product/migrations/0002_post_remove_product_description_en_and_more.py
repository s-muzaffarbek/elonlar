# Generated by Django 4.2 on 2023-04-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_en', models.CharField(max_length=100, null=True)),
                ('title_ru', models.CharField(max_length=100, null=True)),
                ('title_uz', models.CharField(max_length=100, null=True)),
                ('about', models.TextField()),
                ('about_en', models.TextField(null=True)),
                ('about_ru', models.TextField(null=True)),
                ('about_uz', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_uz',
        ),
    ]