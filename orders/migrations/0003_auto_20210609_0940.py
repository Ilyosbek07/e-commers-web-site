# Generated by Django 3.2 on 2021-06-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210609_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oredermodel',
            name='address1',
            field=models.CharField(max_length=30, verbose_name='address1'),
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='address2',
            field=models.CharField(default=2, max_length=30, verbose_name='address2'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='city',
            field=models.CharField(max_length=30, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='last_name',
            field=models.CharField(default=2, max_length=30, verbose_name='last_name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='postcode',
            field=models.CharField(default=1, max_length=30, verbose_name='postcode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='oredermodel',
            name='state',
            field=models.CharField(max_length=30, verbose_name='state'),
        ),
    ]