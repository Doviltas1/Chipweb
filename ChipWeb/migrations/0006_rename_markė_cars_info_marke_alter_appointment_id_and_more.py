# Generated by Django 4.1.4 on 2022-12-07 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChipWeb', '0005_auto_20221205_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars_info',
            old_name='Markė',
            new_name='Marke',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cars_info',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
