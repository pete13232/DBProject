# Generated by Django 3.2.4 on 2021-06-04 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210605_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='picture',
            field=models.ImageField(default='static/images/defaultProfile.png', upload_to='static/images/'),
        ),
    ]