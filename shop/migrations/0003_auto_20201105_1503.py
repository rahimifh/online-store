# Generated by Django 3.1.3 on 2020-11-05 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
