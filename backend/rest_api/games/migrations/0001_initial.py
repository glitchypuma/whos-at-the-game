# Generated by Django 4.2.1 on 2023-05-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseballGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=100)),
                ('away_team', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(db_comment='Date and time baseball game is slated to start.')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
