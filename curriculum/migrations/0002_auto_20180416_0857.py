# Generated by Django 2.0.2 on 2018-04-16 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='time',
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.ManyToManyField(to='curriculum.Time'),
        ),
    ]