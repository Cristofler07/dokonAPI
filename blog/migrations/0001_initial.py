# Generated by Django 5.0.3 on 2024-10-25 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=222)),
                ('kodi', models.CharField(max_length=20)),
                ('umumiySoni', models.IntegerField()),
                ('kelgan_narxi', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Xodim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familiyasi', models.CharField(max_length=20)),
                ('ismi', models.CharField(max_length=20)),
                ('id_raqami', models.CharField(max_length=10)),
                ('oyligi', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kirim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxsulotSoni', models.IntegerField()),
                ('kirim_sana', models.DateTimeField(auto_now_add=True)),
                ('kirim_narxi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maxsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.maxsulot')),
                ('xodim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.xodim')),
            ],
        ),
        migrations.CreateModel(
            name='Chiqim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxsulotSoni', models.IntegerField()),
                ('sotish_narxi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sotish_vaqti', models.DateTimeField(auto_now_add=True)),
                ('maxsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.maxsulot')),
                ('xodim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.xodim')),
            ],
        ),
    ]
