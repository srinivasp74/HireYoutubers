# Generated by Django 3.1.4 on 2020-12-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('detailed_message', models.TextField(blank=True)),
            ],
        ),
    ]
