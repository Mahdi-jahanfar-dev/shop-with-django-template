# Generated by Django 5.1.3 on 2024-12-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_options_product_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='%Y/%m/%d/'),
        ),
    ]
