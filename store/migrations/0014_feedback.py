# Generated by Django 3.1 on 2021-03-24 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(max_length=30)),
                ('line2', models.CharField(max_length=30)),
                ('line3', models.CharField(max_length=30)),
                ('line4', models.CharField(max_length=30)),
                ('F_Name', models.CharField(max_length=70, null=True)),
                ('Email', models.CharField(max_length=70, null=True)),
            ],
        ),
    ]
