# Generated by Django 3.2.3 on 2021-06-18 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0016_auto_20210618_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventconductedordelivered',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='guestlecorganizedordelivered',
            name='user',
            field=models.CharField(default='', max_length=100),
        ),
    ]
