# Generated by Django 4.2.3 on 2023-08-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0004_popular_blogs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='regular_blogs',
            name='image',
            field=models.ImageField(default='', upload_to='myapp2/images'),
        ),
    ]
