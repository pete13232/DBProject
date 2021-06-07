# Generated by Django 3.2.4 on 2021-06-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queueSystem', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='status',
            field=models.CharField(choices=[('success', 'success'), ('fail', 'fail'), ('calling', 'calling'), ('waiting', 'waiting'), ('cancel', 'cancel'), ('point', 'point')], default='waiting', max_length=10),
        ),
    ]
