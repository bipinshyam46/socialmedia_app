# Generated by Django 4.2.5 on 2023-09-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia_app', '0005_alter_users_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.TextField(default='none', max_length=20),
        ),
    ]
