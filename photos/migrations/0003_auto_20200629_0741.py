# Generated by Django 3.0.7 on 2020-06-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20200628_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]
