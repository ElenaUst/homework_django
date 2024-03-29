# Generated by Django 4.2.7 on 2023-12-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('create_date',), 'verbose_name': 'статья', 'verbose_name_plural': 'статьи'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
