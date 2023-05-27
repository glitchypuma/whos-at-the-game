from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for baseballgame
from .serializers import GamesMetaSerializer, BaseballGameSerializer, BasketballGameSerializer, FootballGameSerializer, AmericanFootballGameSerializer
# baseballgame model
from .models import GamesMeta, BaseballGame, BasketballGame, FootballGame, AmericanFootballGame
import requests
from datetime import datetime, timedelta
from django.http import JsonResponse

''' BASEBALL (MLB) '''
@csrf_exempt
def baseball_games_today(request):
    today = datetime.today()
    '''
    Return list of all of today's baseball games
    '''
    if(request.method == 'GET'):
        # does db have today's games?
        processedToday = GamesMeta.objects.filter(date_updated = today.strftime('%Y-%m-%d')).first()
        print(processedToday)

        if(check_exists(processedToday)): #if so, GET baseball games from db
            baseball_games = BaseballGame.objects.filter(date_start = today.strftime('%Y-%m-%d'))
            return JsonResponse(list(baseball_games.values()), safe=False)
        else: #if not, GET baseball games from API and save to db for future retrieval
            # TODO: BETTER KEY MANAGEMENT
            headers = {
                'X-RapidAPI-Key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a', 
                'X-RapidAPI-Host': 'api-baseball.p.rapidapi.com'
                }
            season = today.strftime('%Y')
            params = {
                'timezone': 'America/Los_Angeles',
                'date': today.strftime('%Y-%m-%d'),
                'season': season,
                'league': '1'
            }
            response = requests.get('https://api-baseball.p.rapidapi.com/games', headers=headers, params=params)
            baseball_games = response.json()
            return post_baseball_games(baseball_games)

def post_baseball_games(data):
    parameters = data['parameters']
    raw_games = data['response']
    mapped_baseball_games = [ ]
    for game in raw_games:
        mapped_baseball_games.append({
            'id': game['id'],
            'date_start': parameters['date'],
            'time_start': game['time'],
            'season': parameters['season'],
            'week': game['week'],
            'home_team': game['teams']['home']['name'],
            'away_team': game['teams']['away']['name'],
            'country': game['country']['name'],
            'league': game['league']['name'],
            'completed': True if game['status']['short'] == 'FT' else False
        })

    serializer = BaseballGameSerializer(data=mapped_baseball_games, many=True)
    # check if the sent information is okay
    if(serializer.is_valid()):
        # if okay, save it on the database
        serializer.save()
        update_date()
        # provide a Json Response with the data that was saved
        return JsonResponse(serializer.data, safe=False, status=201)
        # provide a Json Response with the necessary error information
    return JsonResponse(serializer.errors, status=400)
    

''' BASKETBALL (NBA) '''
@csrf_exempt
def basketball_games_today(request):
    today = datetime.today()
    '''
    Return list of all of today's basketball games
    '''
    if(request.method == 'GET'):
        processedToday = GamesMeta.objects.filter(date_updated = today.strftime('%Y-%m-%d')).first()

        if(check_exists(processedToday)):
            basketball_games = BasketballGame.objects.filter(date_start = today.strftime('%Y-%m-%d'))
            return JsonResponse(list(basketball_games.values()), safe=False)
        else:
            headers = {
                'X-RapidAPI-Key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a', 
                'X-RapidAPI-Host': 'api-basketball.p.rapidapi.com'
            }
            season = (today - timedelta(days=365)).strftime('%Y') + "-" + today.strftime('%Y')
            params = {
                'timezone': 'America/Los_Angeles',
                'date': today.strftime('%Y-%m-%d'),
                'season': season,
                'league': '12'
            }
            response = requests.get('https://api-basketball.p.rapidapi.com/games', headers=headers, params=params)
            basketball_games = response.json()
            return post_basketball_games(basketball_games)

def post_basketball_games(data):
    parameters = data['parameters']
    raw_games = data['response']
    mapped_basketball_games = [ ]
    for game in raw_games:
        mapped_basketball_games.append({
            'id': game['id'],
            'date_start': parameters['date'],
            'time_start': game['time'],
            'season': parameters['season'],
            'week': game['week'],
            'home_team': game['teams']['home']['name'],
            'away_team': game['teams']['away']['name'],
            'country': game['country']['name'],
            'league': game['league']['name'],
            'completed': True if game['status']['short'] == 'FT' else False
        })

    # instanciate with the serializer
    serializer = BasketballGameSerializer(data=mapped_basketball_games, many=True)
    # check if the sent information is okay
    if(serializer.is_valid()):
        # if okay, save it on the database
        serializer.save()
        update_date()
        # provide a Json Response with the data that was saved
        return JsonResponse(serializer.data, safe=False, status=201)
        # provide a Json Response with the necessary error information
    return JsonResponse(serializer.errors, status=400)
            
''' FOOTBALL (MLS) '''
@csrf_exempt
def football_games_today(request):
    today = datetime.today()
    '''
    List all of today's football games using API-FOOTBALL
    '''
    if(request.method == 'GET'):
        processedToday = GamesMeta.objects.filter(date_updated = today.strftime('%Y-%m-%d')).first()

        if(check_exists(processedToday)):
            football_games = FootballGame.objects.filter(date_start = today.strftime('%Y-%m-%d'))
            return JsonResponse(list(football_games.values()), safe=False)
        else:
            headers = {
                'X-RapidAPI-Key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a', 
                'X-RapidAPI-Host': 'api-football-v1.p.rapidapi.com'
            }
            season = today.strftime('%Y')
            params = {
                'timezone': 'America/Los_Angeles',
                'date': today.strftime('%Y-%m-%d'),
                'season': season,
                'league': '253'
            }
            response = requests.get('https://api-football-v1.p.rapidapi.com/v3/fixtures', headers=headers, params=params)
            football_games = response.json()
            return post_football_games(football_games)
def post_football_games(data):
    parameters = data['parameters']
    raw_games = data['response']
    mapped_football_games = [ ]
    for game in raw_games:
        mapped_football_games.append({
            'id': game['fixture']['id'],
            'date_start': parameters['fixture']['date'],
            'time_start': game['fixture']['timestamp'],
            'season': parameters['fixture']['league']['season'],
            'round': game['fixture']['league']['round'],
            'home_team': game['fixture']['teams']['home']['name'],
            'away_team': game['fixture']['teams']['away']['name'],
            'country': game['fixture']['league']['country'],
            'league': game['fixture']['league']['name'],
            'completed': True if game['fixture']['status']['short'] == 'FT' else False
        })
    serializer = FootballGameSerializer(data=mapped_football_games, many=True)
    # check if the sent information is okay
    if(serializer.is_valid()):
        # if okay, save it on the database
        serializer.save()
        update_date()
        # provide a Json Response with the data that was saved
        return JsonResponse(serializer.data, safe=False, status=201)
        # provide a Json Response with the necessary error information
    return JsonResponse(serializer.errors, status=400)   



''' AMERICAN FOOTBALL '''
@csrf_exempt
def ame_football_games_today(request, league):
    today = datetime.today()

    '''
    Return list of all of today's basketball games
    '''
    if(request.method == 'GET'):
        processedToday = GamesMeta.objects.filter(date_updated = today.strftime('%Y-%m-%d')).first()

        if(check_exists(processedToday)):
            american_football_games = AmericanFootballGame.objects.filter(date_start = today.strftime('%Y-%m-%d'))
            return JsonResponse(list(american_football_games.values()), safe=False)
        else:
            headers = {
                'X-RapidAPI-Key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a', 
                'X-RapidAPI-Host': 'api-american-football.p.rapidapi.com'
            }
            match league:
                    case 1:
                        # NFL seasons run Sept-Jan, so season year can fall in the next year
                        # hacky-solution is to subtract 60 days before evaluating season year
                        season = (datetime.today() - timedelta(days=60)).strftime('%Y') 
                    case 2:
                        # NCAA seasons runs Aug-Dec, so season year will always fall on today's year
                        season =  datetime.today().strftime('%Y')
            params = {
                'timezone': 'America/Los_Angeles',
                'date': today,
                'season': season,
                'league': str(league)
            }
            response = requests.get('https://api-american-football.p.rapidapi.com/games', headers=headers, params=params)
            american_football_games = response.json()
            return post_american_football_games(american_football_games)
def post_american_football_games(data):
    parameters = data['parameters']
    raw_games = data['response']
    mapped_american_football_games = [ ]
    for game in raw_games:
        mapped_american_football_games.append({
            'id': game['game']['id'],
            'date_start': parameters['date'],
            'time_start': game['date']['time'],
            'season': parameters['season'],
            'week': game['game']['week'],
            'home_team': game['teams']['home']['name'],
            'away_team': game['teams']['away']['name'],
            'country': game['league']['name'],
            'league': game['league']['country']['name'],
            'completed': True if game['game']['status']['short'] == 'FT' else False
        })
    serializer = AmericanFootballGameSerializer(data=mapped_american_football_games, many=True)
    if(serializer.is_valid()):
        serializer.save()
        update_date()
        return JsonResponse(serializer.data, safe=False, status=201)
    return JsonResponse(serializer.errors, status=400)
        
''' UTILS '''
def check_exists(data):
    try:
        data.id
    except AttributeError:
        return False
    else:
        return True
    
def update_date():
    date = {
        'date_updated': datetime.today().strftime('%Y-%m-%d')
    }
    serializer = GamesMetaSerializer(data=date, many=False)
    if(serializer.is_valid()):
        serializer.save()
        return JsonResponse(serializer.data, safe=False, status=201)
    return JsonResponse(serializer.errors, status=400)