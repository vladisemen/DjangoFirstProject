# Generated by Django 3.1.3 on 2020-12-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produckt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('categories', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
