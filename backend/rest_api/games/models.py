from django.db import models

class BaseballGame(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    start_time = models.DateTimeField(
    db_comment="Date and time baseball game is slated to start.",
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.away_team + "@" + self.home_team