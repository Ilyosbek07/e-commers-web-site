# Generated by Django 3.2 on 2021-06-05 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0018_alter_wishlistmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimagemodel',
            options={'verbose_name': 'product image', 'verbose_name_plural': 'product images'},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='wishlist',
            field=models.ManyToManyField(related_name='wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='code',
            field=models.CharField(max_length=10, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='productimagemodel',
            name='image',
            field=models.ImageField(upload_to='products', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.brandmodel', verbose_name='brand'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='short_description',
            field=models.TextField(verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='short_description_en',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='short_description_uz',
            field=models.TextField(null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='sizemodel',
            name='title',
            field=models.CharField(max_length=3, verbose_name='title'),
        ),
        migrations.DeleteModel(
            name='WishlistModel',
        ),
    ]
