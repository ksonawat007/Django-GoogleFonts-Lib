# Generated by Django 3.1.5 on 2021-03-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databasedesign', '0004_auto_20210307_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='subsets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsets', models.CharField(blank=True, max_length=25)),
            ],
        ),
    ]