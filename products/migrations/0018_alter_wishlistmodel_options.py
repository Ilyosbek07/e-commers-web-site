# Generated by Django 3.2 on 2021-06-02 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_wishlistmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlistmodel',
            options={'verbose_name': 'wishlist', 'verbose_name_plural': 'wishlists'},
        ),
    ]