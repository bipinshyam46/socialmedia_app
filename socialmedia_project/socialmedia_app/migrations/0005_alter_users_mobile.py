# Generated by Django 4.2.5 on 2023-09-12 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia_app', '0004_alter_users_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.IntegerField(default=9, max_length=20),
        ),
    ]