# Generated by Django 3.2 on 2021-06-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oredermodel',
            name='address1',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='address1'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='address2',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='address2'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='country',
            field=models.CharField(default=2, max_length=30, verbose_name='country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first_name'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='last_name'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='postcode',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='postcode'),
        ),
        migrations.AddField(
            model_name='oredermodel',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='state'),
        ),
    ]
