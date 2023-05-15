from rest_framework import routers,serializers,viewsets
from .models import BaseballGame
class BaseballGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseballGame
        fields = ['id', 'home_team', 'away_team', 'start_time', 'completed']