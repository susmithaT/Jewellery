# Generated by Django 3.0.3 on 2020-04-18 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(default='', max_length=25, primary_key=True, serialize=False)),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metal', models.CharField(default='', max_length=10)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(default='', max_length=25)),
                ('price', models.IntegerField()),
                ('place', models.CharField(max_length=25)),
                ('orderdate', models.DateTimeField(auto_now_add=True)),
                ('item', models.ManyToManyField(default='', to='collection.Item')),
                ('metal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Material')),
            ],
        ),
    ]
