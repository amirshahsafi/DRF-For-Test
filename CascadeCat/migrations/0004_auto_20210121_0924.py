# Generated by Django 3.1.4 on 2021-01-21 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CascadeCat', '0003_product_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='main_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CascadeCat.category', verbose_name='category from'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(to='CascadeCat.SubCategory', verbose_name='Sub Category'),
        ),
    ]