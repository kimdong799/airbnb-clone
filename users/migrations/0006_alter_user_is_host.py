# Generated by Django 5.0.1 on 2024-03-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_is_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_host',
            field=models.BooleanField(default=False),
        ),
    ]
