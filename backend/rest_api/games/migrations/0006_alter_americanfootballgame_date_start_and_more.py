# Generated by Django 4.2.1 on 2023-05-22 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_alter_basketballgame_time_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='americanfootballgame',
            name='date_start',
            field=models.DateField(db_comment='Date football game is slated to start, formatted as YYYY-mm-dd', default='2023-05-21'),
        ),
        migrations.AlterField(
            model_name='baseballgame',
            name='date_start',
            field=models.DateField(db_comment='Date baseball game is slated to start, formatted as YYYY-mm-dd', default='2023-05-21'),
        ),
        migrations.AlterField(
            model_name='basketballgame',
            name='date_start',
            field=models.DateField(db_comment='Date basketball game is slated to start, formatted as YYYY-mm-dd', default='2023-05-21'),
        ),
        migrations.AlterField(
            model_name='footballgame',
            name='date_start',
            field=models.DateField(db_comment='Date football game is slated to start, formatted as YYYY-mm-dd', default='2023-05-21'),
        ),
    ]
