# Generated by Django 5.1 on 2024-08-24 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_dados_delete_sobremim'),
    ]

    operations = [
        migrations.CreateModel(
            name='foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='foto/')),
            ],
        ),
    ]
