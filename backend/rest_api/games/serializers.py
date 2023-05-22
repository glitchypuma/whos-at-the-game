from rest_framework import routers,serializers,viewsets
from .models import BaseballGame, BasketballGame, FootballGame
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