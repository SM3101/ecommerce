# Generated by Django 4.2.4 on 2023-12-09 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_products_display_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='display_id',
        ),
    ]
