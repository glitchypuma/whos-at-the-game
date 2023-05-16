from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for baseballgame
from .serializers import BaseballGameSerializer
# baseballgame model
from .models import BaseballGame
import requests
from datetime import datetime

from django.http import JsonResponse

@csrf_exempt
def baseball_games_today(request):
    # TODO: BETTER KEY MANAGEMENT
    headers = {
        'X-RapidAPI-Key': 'e0a8f66d5dmsh53685da2f2425e3p138e6cjsnd3a33ec1fb3a', 
        'X-RapidAPI-Host': 'api-baseball.p.rapidapi.com'
        }
    
    today = datetime.today().strftime('%Y-%m-%d')
    season = datetime.today().strftime('%Y')
    params = {
        'timezone': 'America/Los_Angeles',
        'date': today,
        'season': season,
        'league': '1'
    }

    '''
    List all of today's baseball games using API-BASEBALL
    '''
    if(request.method == 'GET'):
        # print(params)
        # get all the baseball games
        response = requests.get('https://api-baseball.p.rapidapi.com/games', headers=headers, params=params)
        baseball_games = response.json()
        
        return JsonResponse(baseball_games) #TODO: use serializer + model

    #     games = BaseballGame.objects.all()
    #     # serialize the task data
    #     serializer = BaseballGameSerializer(games, many=True)
    #     # return a Json response
    #     return JsonResponse(serializer.data,safe=False)
    # elif(request.method == 'POST'):
    #     # parse the incoming information
    #     data = JSONParser().parse(request)
    #     # instanciate with the serializer
    #     serializer = BaseballGameSerializer(data=data)
    #     # check if the sent information is okay
    #     if(serializer.is_valid()):
    #         # if okay, save it on the database
    #         serializer.save()
    #         # provide a Json Response with the data that was saved
    #         return JsonResponse(serializer.data, status=201)
    #         # provide a Json Response with the necessary error information
    #     return JsonResponse(serializer.errors, status=400)
    
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