# Generated by Django 4.2.4 on 2023-12-02 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_products_subcategory_products_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]