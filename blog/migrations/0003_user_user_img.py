# Generated by Django 3.2.20 on 2023-08-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_user_user_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to='user_img'),
        ),
    ]
