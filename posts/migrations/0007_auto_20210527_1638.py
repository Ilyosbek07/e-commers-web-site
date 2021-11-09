# Generated by Django 3.2 on 2021-05-27 11:38

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='content_uz',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_en',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='title_uz',
            field=models.CharField(max_length=30, null=True, verbose_name='title'),
        ),
    ]
