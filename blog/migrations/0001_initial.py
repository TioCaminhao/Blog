# Generated by Django 5.1 on 2024-08-24 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('cell', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sobremim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto1', models.TextField()),
                ('texto2', models.TextField()),
            ],
        ),
    ]
