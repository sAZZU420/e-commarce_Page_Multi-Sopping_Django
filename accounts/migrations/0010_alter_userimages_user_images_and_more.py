# Generated by Django 5.0.4 on 2024-08-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_userimages_user_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimages',
            name='user_images',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/<django.db.models.query_utils.DeferredAttribute object at 0x000002354E12B320>'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cover_pic/<django.db.models.query_utils.DeferredAttribute object at 0x000002354E12B320>'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic/<django.db.models.query_utils.DeferredAttribute object at 0x000002354E12B320>'),
        ),
    ]