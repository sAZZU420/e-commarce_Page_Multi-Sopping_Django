# Generated by Django 5.0.4 on 2024-07-25 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_review_status_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_date'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
