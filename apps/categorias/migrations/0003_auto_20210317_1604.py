# Generated by Django 3.0 on 2021-03-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redacción',
            name='fecha',
            field=models.DateTimeField(),
        ),
    ]