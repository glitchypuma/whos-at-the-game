from django.db import models

# Create your models here.
class Scraper(models.Model):
    query = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.query
