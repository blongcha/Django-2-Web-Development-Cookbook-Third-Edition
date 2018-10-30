# Generated by Django 2.1.1 on 2018-09-20 04:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['rank', 'title', '-release_year'], 'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
        migrations.AddField(
            model_name='movie',
            name='rank',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.PositiveSmallIntegerField(default=2018, validators=[django.core.validators.MinValueValidator(1888), django.core.validators.MaxValueValidator(2018)], verbose_name='Release year'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Rating'),
        ),
    ]