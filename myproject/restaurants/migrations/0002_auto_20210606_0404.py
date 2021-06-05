# Generated by Django 3.2.4 on 2021-06-05 21:04

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='coverPic',
            field=imagekit.models.fields.ProcessedImageField(upload_to='static/images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='company',
            name='profilePic',
            field=imagekit.models.fields.ProcessedImageField(upload_to='static/images/%Y/%m/%d'),
        ),
    ]
