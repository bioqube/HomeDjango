# Generated by Django 4.2.7 on 2024-01-16 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'product',
            },
        ),
    ]
