# Generated by Django 5.1.5 on 2025-02-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_articleimage_delete_articlefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(upload_to='news_files/', verbose_name='Image'),
        ),
    ]
