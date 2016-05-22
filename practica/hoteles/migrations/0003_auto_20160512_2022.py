# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0002_auto_20160428_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hid', models.IntegerField(default=0)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='HotelsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=300)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hid', models.IntegerField(default=0)),
                ('url', models.URLField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PagUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=300)),
                ('title', models.CharField(default='', max_length=300)),
                ('color', models.CharField(default='', max_length=300)),
                ('size', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='body',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='subcategoria',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='web',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='hotel',
            name='source',
            field=models.URLField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='hotel',
            name='stars',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='hotel',
            name='url',
            field=models.URLField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='tipo',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Imagenes',
        ),
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoteles.Hotel'),
        ),
        migrations.AddField(
            model_name='hotelsuser',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoteles.Hotel'),
        ),
        migrations.AddField(
            model_name='comment',
            name='com',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoteles.Hotel'),
        ),
    ]
