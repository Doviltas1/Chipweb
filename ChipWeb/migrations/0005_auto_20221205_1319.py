# Generated by Django 2.2.14 on 2022-12-05 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChipWeb', '0004_cars_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars_info',
            old_name='Make',
            new_name='Markė',
        ),
    ]
