# Generated by Django 3.2.8 on 2021-10-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='ciudad',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='continente',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='pais',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='region',
            field=models.CharField(max_length=40),
        ),
    ]
