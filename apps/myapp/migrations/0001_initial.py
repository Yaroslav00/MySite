# Generated by Django 2.1.5 on 2019-01-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=100)),
                ('file', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
