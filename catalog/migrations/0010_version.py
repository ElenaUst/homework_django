# Generated by Django 4.2.7 on 2023-12-23 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, verbose_name='Номер версии')),
                ('name', models.CharField(max_length=150, verbose_name='Название версии')),
                ('is_active', models.BooleanField(default=True, verbose_name='Признак текущей версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]
