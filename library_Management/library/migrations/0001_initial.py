# Generated by Django 3.2.8 on 2021-11-11 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=50)),
                ('b_author', models.CharField(max_length=30)),
                ('b_title', models.TextField(max_length=150)),
                ('publish_date', models.DateField(default=datetime.date(2021, 11, 11))),
                ('b_image', models.ImageField(max_length=150, upload_to='book_images')),
            ],
        ),
    ]
