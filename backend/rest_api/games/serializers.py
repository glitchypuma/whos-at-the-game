from rest_framework import routers,serializers,viewsets
from .models import GamesMeta, BaseballGame, BasketballGame, FootballGame, AmericanFootballGame

class GamesMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GamesMeta
        fields = ['sport', 'league', 'date_updated']
class BaseballGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseballGame
        fields = ['id', 'date_start', 'time_start', 'season', 'week', 'home_team', 'away_team', 'country', 'league', 'completed']

class BasketballGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BasketballGame
        fields = ['id', 'date_start', 'time_start', 'season', 'week', 'home_team', 'away_team', 'country', 'league', 'completed']

class FootballGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FootballGame
        fields = ['id', 'date_start', 'time_start', 'season', 'round', 'home_team', 'away_team', 'country', 'league', 'completed']

class AmericanFootballGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmericanFootballGame
        fields = ['id', 'date_start', 'time_start', 'season', 'week', 'home_team', 'away_team', 'country', 'league', 'completed']