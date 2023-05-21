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
        return mapped_baseball_game

    class Meta:
        model = BaseballGame
        fields = ['id', 'date_start', 'time_start', 'season', 'week', 'home_team', 'away_team', 'country', 'league', 'completed']

class BasketballGameSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, data, parameters):
        mapped_basketball_game = {
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
        return mapped_basketball_game

    class Meta:
        model = BaseballGame
        fields = ['id', 'date_start', 'time_start', 'season', 'week', 'home_team', 'away_team', 'country', 'league', 'completed']

class FootballGameSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, data, parameters):
        mapped_football_game = {
            'id': data.id,
            'date_start': parameters.date,
            'time_start': data.fixture.timestamp,
            'season': parameters.season,
            'round': data.league.round,
            'home_team': data.fixture.teams.home.name,
            'away_team': data.teams.away.name,
            'country': data.league.country,
            'league': data.league.name,
            'completed': True if data.fixture.status.short=='FT' else False
        }
        return mapped_football_game

    class Meta:
        model = BaseballGame
        fields = ['id', 'date_start', 'time_start', 'season', 'round', 'home_team', 'away_team', 'country', 'league', 'completed']