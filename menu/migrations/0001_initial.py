# Generated by Django 4.2.7 on 2023-11-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam_product', models.CharField(max_length=225)),
                ('harga', models.IntegerField()),
            ],
        ),
    ]