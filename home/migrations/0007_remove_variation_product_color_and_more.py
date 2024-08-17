# Generated by Django 5.0.4 on 2024-08-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='product_color',
        ),
        migrations.RemoveField(
            model_name='variation',
            name='product_size',
        ),
        migrations.AddField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(default=None, max_length=100),
        ),
    ]