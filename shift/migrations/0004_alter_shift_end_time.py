# Generated by Django 4.0.4 on 2022-09-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0003_alter_shift_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
