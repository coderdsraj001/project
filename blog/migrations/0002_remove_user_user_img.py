# Generated by Django 3.2.20 on 2023-08-30 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_img',
        ),
    ]
