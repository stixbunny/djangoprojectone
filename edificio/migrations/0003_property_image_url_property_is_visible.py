# Generated by Django 4.2.2 on 2023-06-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edificio', '0002_alter_property_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='is_visible',
            field=models.BooleanField(null=True),
        ),
    ]
