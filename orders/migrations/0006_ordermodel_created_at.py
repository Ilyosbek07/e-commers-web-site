# Generated by Django 3.2 on 2021-06-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_oredermodel_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=2, verbose_name='created_at'),
            preserve_default=False,
        ),
    ]
