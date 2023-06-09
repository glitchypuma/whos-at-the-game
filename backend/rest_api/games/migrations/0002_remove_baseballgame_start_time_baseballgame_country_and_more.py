# Generated by Django 4.2.1 on 2023-05-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseballgame',
            name='start_time',
        ),
        migrations.AddField(
            model_name='baseballgame',
            name='country',
            field=models.CharField(db_comment='The country this game is taking place in', null=True),
        ),
        migrations.AddField(
            model_name='baseballgame',
            name='date_start',
            field=models.DateTimeField(db_comment='Date and time baseball game is slated to start', default='2023-05-21'),
        ),
        migrations.AddField(
            model_name='baseballgame',
            name='league',
            field=models.CharField(null=True),
        ),
        migrations.AddField(
            model_name='baseballgame',
            name='season',
            field=models.CharField(default='2023', max_length=50),
        ),
        migrations.AddField(
            model_name='baseballgame',
            name='time_start',
            field=models.CharField(db_comment='Time baseball game is slated to start, formatted as hh:mm', null=True),
        ),
    ]
