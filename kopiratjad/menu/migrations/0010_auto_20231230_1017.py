# Generated by Django 3.0 on 2023-12-30 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formlogin',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
