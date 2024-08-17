# Generated by Django 5.0.4 on 2024-07-23 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_review_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]