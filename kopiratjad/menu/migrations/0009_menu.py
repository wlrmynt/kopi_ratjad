# Generated by Django 3.2 on 2023-12-29 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_product', models.CharField(max_length=225)),
                ('harga', models.IntegerField()),
                ('air', models.CharField(max_length=20)),
                ('jenis_gilingan_biji_kopi', models.CharField(max_length=20)),
                ('takaran_gula', models.CharField(max_length=40)),
                ('takaran_susu', models.CharField(max_length=40)),
                ('takaran_soda', models.CharField(max_length=40)),
                ('takaran_marjan', models.CharField(max_length=40)),
                ('keterangan', models.TextField()),
                ('status', models.CharField(choices=[('menu', 'Menu'), ('in_progress', 'In progress'), ('closed', 'Closed')], default='menu', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Menu',
            },
        ),
    ]
