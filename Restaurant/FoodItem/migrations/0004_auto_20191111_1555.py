# Generated by Django 2.2.6 on 2019-11-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodItem', '0003_auto_20191110_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='assigned',
            field=models.CharField(default='', max_length=30),
        ),
    ]
