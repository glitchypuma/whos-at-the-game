from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for baseballgame
from .serializers import BaseballGameSerializer, BasketballGameSerializer
# baseballgame model
from .models import BaseballGame, BasketballGame
import requests
from datetime import datetime, timedelta
from django.http import JsonResponse

# TODO: BETTER KEY MANAGEMENT
headers = {
    'X-RapidAPI-Key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a', 
    'X-RapidAPI-Host': 'api-baseball.p.rapidapi.com'
    }


''' BASEBALL (MLB) '''
@csrf_exempt
def baseball_games_today(request):
    today = datetime.today().strftime('%Y-%m-%d')
    
    '''
    Return list of all of today's baseball games
    '''
    if(request.method == 'GET'):
        # does db have today's games? 
        baseballGame = BaseballGame.objects.first
        serializedGame = BaseballGameSerializer(baseballGame, many=False)
        if(serializedGame.date_start == today): #if so, GET baseball games from db
            baseball_games = BaseballGame.objects.all()
            serializer = BaseballGameSerializer(baseball_games, many=True)
            return JsonResponse(serializer.data,safe=False)
        else: #if not, GET baseball games from API and save to db for future retrieval
            season = datetime.today().strftime('%Y')
            params = {
                'timezone': 'America/Los_Angeles',
                'date': today,
                'season': season,
                'league': '1'
            }
            response = requests.get('https://api-baseball.p.rapidapi.com/games', headers=headers, params=params)
            baseball_games = response.json()
            serializer = BaseballGameSerializer(data=baseball_games.data, many=True)
            
            post_baseball_game(data=baseball_games.data)

            # check if the information received is okay
            # if(post_response.status ?)
            return JsonResponse(serializer.data, safe=False)
            
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = BaseballGameSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

def post_baseball_game(response):
    # parse the incoming information
    data = JSONParser().parse(response)
    # instanciate with the serializer
    serializer = BaseballGameSerializer(data=data)
    # check if the sent information is okay
    if(serializer.is_valid()):
        # if okay, save it on the database
        serializer.save()
        # provide a Json Response with the data that was saved
        return JsonResponse(serializer.data, status=201)
        # provide a Json Response with the necessary error information
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def baseball_game_detail(request, pk):
    try:
        # obtain the baseball game with the passed id.
        game = BaseballGame.objects.get(pk=pk)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = BaseballGamekSerializer(task, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the task
        game.delete() 
        # return a no content response.
        return HttpResponse(status=204)
    
''' BASKETBALL (NBA) '''
@csrf_exempt
def basketball_games_today(request):
    today = datetime.today().strftime('%Y-%m-%d')

    '''
    Return list of all of today's basketball games
    '''
    if(request.method == 'GET'):
        basketballGame = BasketballGame.objects.first
        serializedGame = BasketballGameSerializer(basketballGame, many=False)
        if(serializedGame.date_start == today):
            basketball_games = BasketballGame.objects.all()
            serializer = BasketballGameSerializer(basketball_games, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            season = (datetime.today() - timedelta(days=365)).strftime('%Y') + "-" + datetime.today().strftime('%Y')
            params = {
                'timezone': 'America/Los_Angeles',
                'date': today,
                'season': season,
                'league': '12'
            }
            response = requests.get('https://api-basketball.p.rapidapi.com/games', headers=headers, params=params)
            basketball_games = response.json()
            serializer = BasketballGameSerializer(data=basketball_games, many=True)

            post_basketball_game(data=basketball_games.data, many=True)
            # check if the information received is okay
            # if(post_response.status ?)
            return JsonResponse(serializer.data, safe=False)

def post_baseball_game(response):
    # parse the incoming information
    data = JSONParser().parse(response)
    # instanciate with the serializer
    serializer = BasketballGameSerializer(data=data)
    # check if the sent information is okay
    if(serializer.is_valid()):
        # if okay, save it on the database
        serializer.save()
        # provide a Json Response with the data that was saved
        return JsonResponse(serializer.data, status=201)
        # provide a Json Response with the necessary error information
    return JsonResponse(serializer.errors, status=400)
            
''' FOOTBALL (MLS) '''

@csrf_exempt
def football_games_today(request):
    today = datetime.today().strftime('%Y-%m-%d')
    season = datetime.today().strftime('%Y')
    params = {
        'timezone': 'America/Los_Angeles',
        'date': today,
        'season': season,
        'league': '253'
    }

    '''
    List all of today's football games using API-FOOTBALL
    '''
    if(request.method == 'GET'):
        # get all the football games
        response = requests.get('https://api-football-v1.p.rapidapi.com/v3/fixtures', headers=headers, params=params)
        football_games = response.json()
        
        return JsonResponse(football_games) #TODO: use serializer + model
    
''' AMERICAN FOOTBALL '''

@csrf_exempt
def ame_football_games_today(request, league):
    ### Set request parameters
    today = datetime.today().strftime('%Y-%m-%d')
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

    '''
    List all of today's football games for given league using API-FOOTBALL
    '''
    if(request.method == 'GET'):
        # get all the football games
        response = requests.get('https://api-american-football.p.rapidapi.com/games', headers=headers, params=params)
        ame_football_games = response.json()

        if(JsonResponse(ame_football_games).getvalue != 0):
            return JsonResponse(ame_football_games) #TODO: use serializer + model