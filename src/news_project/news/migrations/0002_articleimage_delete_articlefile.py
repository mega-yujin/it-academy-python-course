# Generated by Django 5.1.5 on 2025-02-14 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/', verbose_name='Image')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Upload date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='news.article', verbose_name='Article')),
            ],
            options={
                'verbose_name': 'Article image',
                'verbose_name_plural': 'Article images',
            },
        ),
        migrations.DeleteModel(
            name='ArticleFile',
        ),
    ]
