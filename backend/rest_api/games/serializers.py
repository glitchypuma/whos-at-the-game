from rest_framework import routers,serializers,viewsets
from .models import BaseballGame
class BaseballGameSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, data, parameters):
        mapped_baseball_game = {
            'id': data.id,
            'date_start': parameters.date,
            'time_start': data.time,
            'season': parameters.season,
            'week': data.week,
            'home_team': data.teams.home.name,
            'away_team': data.teams.away.name,
            'country': data.country.name,
            'league': data.league.name,
            'completed': True if data.status.short=='FT' else False
        }

    class Meta:
        model = BaseballGame
        fields = ['id', 'date_start', 'time_start', 'week', 'home_team', 'away_team', 'country', 'league', 'completed']