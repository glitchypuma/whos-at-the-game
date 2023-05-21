from django.db import models
from datetime import datetime, timedelta

def get_default_date_start():
    return datetime.today().strftime('%Y-%m-%d')

class BaseballGame(models.Model):
    date_start = models.DateTimeField(default= get_default_date_start(), db_comment="Date baseball game is slated to start, formatted as YYYY-mm-dd")
    time_start = models.CharField(null=True, db_comment="Time baseball game is slated to start, formatted as hh:mm")
    season = models.CharField(null=True, max_length=50)
    week = models.CharField(null=True)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    country = models.CharField(null=True, db_comment="The country this game is taking place in")
    league = models.CharField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.away_team + "@" + self.home_team
    
class BasketballGame(models.Model):
    date_start = models.DateTimeField(default= get_default_date_start(), db_comment="Date basketball game is slated to start, formatted as YYYY-mm-dd")
    time_start = models.CharField(null=True, db_comment="Time baseball game is slated to start, formatted as hh:mm")
    season = models.CharField(null=True, max_length=50)
    week = models.CharField(null=True)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    country = models.CharField(null=True, db_comment="The country this game is taking place in")
    league = models.CharField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.away_team + "@" + self.home_team
    
class FootballGame(models.Model):
    date_start = models.DateTimeField(default= get_default_date_start(), db_comment="Date football game is slated to start, formatted as YYYY-mm-dd")
    time_start = models.TimeField(null=True, db_comment="Time baseball game is slated to start in Timestamp")
    season = models.CharField(null=True, max_length=50)
    round = models.CharField(null=True)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    country = models.CharField(null=True, db_comment="The country this game is taking place in")
    league = models.CharField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.away_team + "@" + self.home_team
    
class AmericanFootballGame(models.Model):
    date_start = models.DateTimeField(default= get_default_date_start(), db_comment="Date football game is slated to start, formatted as YYYY-mm-dd")
    time_start = models.CharField(null=True, db_comment="Time baseball game is slated to start, formatted as hh:mm")
    season = models.CharField(null=True, max_length=50)
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    country = models.CharField(null=True, db_comment="The country this game is taking place in")
    league = models.CharField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.away_team + "@" + self.home_team