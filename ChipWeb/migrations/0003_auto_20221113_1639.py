# Generated by Django 2.2.14 on 2022-11-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChipWeb', '0002_alter_appointment_accepted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
