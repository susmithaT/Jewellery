# Generated by Django 2.2.10 on 2020-04-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.FloatField(verbose_name='weigth(gms)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='collection.Item'),
        ),
    ]
