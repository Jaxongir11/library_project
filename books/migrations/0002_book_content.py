# Generated by Django 4.2.5 on 2023-10-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='Hamma uchun ajoyib kitob'),
            preserve_default=False,
        ),
    ]
