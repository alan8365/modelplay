# Generated by Django 2.0.2 on 2018-04-16 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=20)),
                ('period', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='time',
            unique_together={('week', 'period')},
        ),
        migrations.AddField(
            model_name='course',
            name='time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.Time'),
        ),
    ]