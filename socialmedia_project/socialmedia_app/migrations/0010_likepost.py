# Generated by Django 4.2.5 on 2023-09-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia_app', '0009_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likepost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
