# Generated by Django 4.2.4 on 2023-11-25 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='website.category'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]