# Generated by Django 4.2.16 on 2024-10-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='valoracion',
            field=models.IntegerField(help_text='Valoración entre 0 y 10000'),
        ),
    ]
