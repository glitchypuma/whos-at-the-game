# Generated by Django 4.2.1 on 2023-05-27 03:07

from django.db import migrations, models
import games.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_americanfootballgame_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamesMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateField(default=games.models.get_default_date_start)),
            ],
        ),
        migrations.AlterField(
            model_name='americanfootballgame',
            name='date_start',
            field=models.DateField(db_comment='Date football game is slated to start, formatted as YYYY-mm-dd', default='2023-05-26'),
        ),
        migrations.AlterField(
            model_name='baseballgame',
            name='date_start',
            field=models.DateField(db_comment='Date baseball game is slated to start, formatted as YYYY-mm-dd', default='2023-05-26'),
        ),
        migrations.AlterField(
            model_name='basketballgame',
            name='date_start',
            field=models.DateField(db_comment='Date basketball game is slated to start, formatted as YYYY-mm-dd', default='2023-05-26'),
        ),
        migrations.AlterField(
            model_name='footballgame',
            name='date_start',
            field=models.DateField(db_comment='Date football game is slated to start, formatted as YYYY-mm-dd', default='2023-05-26'),
        ),
    ]