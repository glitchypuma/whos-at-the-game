# Generated by Django 4.2.1 on 2023-05-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_gamesmeta_league_gamesmeta_sport_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesmeta',
            name='date_updated',
            field=models.DateField(default='2023-05-27'),
        ),
    ]
