# Generated by Django 3.2.3 on 2021-05-31 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('detail', models.CharField(max_length=200)),
                ('rating', models.FloatField(default=0)),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.member')),
                ('resID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('queueID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('peopleNum', models.IntegerField(default=0)),
                ('queueCreated', models.DateTimeField(auto_now_add=True)),
                ('reserveTime', models.DateTimeField(blank=True, null=True)),
                ('queueIsSuccess', models.CharField(choices=[('S', 'Success'), ('F', 'Fail'), ('C', 'Cancel'), ('P', 'Point')], max_length=10)),
                ('queueIsCome', models.BooleanField()),
                ('memberID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.member')),
                ('resID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
            options={
                'db_table': 'queue',
            },
        ),
    ]