# Generated by Django 5.1.5 on 2025-02-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookPlatform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_lended',
            field=models.BooleanField(default=False),
        ),
    ]
