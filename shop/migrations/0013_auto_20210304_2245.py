# Generated by Django 3.1.7 on 2021-03-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210104_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wholesale_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
