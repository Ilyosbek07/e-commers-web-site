# Generated by Django 3.2 on 2021-05-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210523_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='size',
            field=models.ManyToManyField(related_name='products', to='products.SizeModel'),
        ),
    ]
