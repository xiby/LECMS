# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 01:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bidTable',
            fields=[
                ('bidNUM', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('costTime', models.FloatField()),
                ('mark', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='carTable',
            fields=[
                ('carNUM', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('avaiable', models.BooleanField()),
                ('city', models.IntegerField()),
                ('load', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ComTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ComID', models.CharField(max_length=10)),
                ('ComPSW', models.CharField(max_length=15)),
                ('ComName', models.CharField(max_length=20)),
                ('ComArea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustID', models.CharField(max_length=10)),
                ('CustPSW', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='invTable',
            fields=[
                ('invNUM', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('startPoint', models.IntegerField()),
                ('destination', models.IntegerField()),
                ('weight', models.FloatField()),
                ('state', models.BooleanField()),
                ('invCust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.CustTable')),
            ],
        ),
        migrations.CreateModel(
            name='orderTable',
            fields=[
                ('orderNUM', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('startPoint', models.IntegerField()),
                ('destination', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('startDate', models.DateField()),
                ('costTime', models.IntegerField()),
                ('state', models.CharField(max_length=10)),
                ('loginfo', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='psw',
            new_name='pwd',
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('orderNUM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myApp.orderTable')),
                ('info', models.CharField(max_length=100)),
                ('replyinfo', models.CharField(max_length=100)),
                ('state', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='ordertable',
            name='ComID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.ComTable'),
        ),
        migrations.AddField(
            model_name='ordertable',
            name='CustID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.CustTable'),
        ),
        migrations.AddField(
            model_name='cartable',
            name='comID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.ComTable'),
        ),
        migrations.AddField(
            model_name='bidtable',
            name='bidCom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myApp.ComTable'),
        ),
    ]
