# Generated by Django 4.2.4 on 2023-08-31 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('qualifications', models.TextField()),
            ],
        ),
    ]
