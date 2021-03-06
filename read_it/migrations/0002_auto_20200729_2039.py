# Generated by Django 3.0.8 on 2020-07-30 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_it', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image_link',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='synopsis',
            field=models.TextField(default='N/A'),
        ),
    ]
