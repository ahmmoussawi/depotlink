# Generated by Django 5.0.1 on 2024-01-27 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_category_image_alter_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='hscode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
