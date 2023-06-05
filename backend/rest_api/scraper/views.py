import json
import sys
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
import pandas as pd
from django.http import HttpResponse, JsonResponse
import requests
from . import nlp

def get_guess(request, away, home):
    if(request.method == 'GET'):
        tweets_str = scrape_twitter(away, home)
        # people_str = nlp.get_names(tweets_str)
        people_list = nlp.get_names(tweets_str)

        mapped_guesses = [ ]
        for person in people_list:
            mapped_guesses.append({
                'name': person,
                'rank': None
            })
        return JsonResponse(data=mapped_guesses, safe=False, status=201)
    else:
        return JsonResponse(status=400)

#snscraper dev version: 0.6.2.20230321.dev12+gea49c19

# Create your views here.
#def scrape_twitter(request, away, home):
def scrape_twitter(away, home):

    scraper = sntwitter.TwitterSearchScraper(home + " " + away)

    tweets = []

    for i, tweet in enumerate(scraper.get_items()):
        # data = [tweet.date, 
        #         tweet.id, 
        #         tweet.rawContent, 
        #         tweet.user.username, 
        #         tweet.likeCount, 
        #         tweet.retweetCount
        # ]
        data = tweet.rawContent
        tweets.append(data)
        if i > 1000:
            break

    # tweets_df = pd.DataFrame(tweets, columns=['date', 'id', 'content', 'username', 
    #                                             'like_count', 'retweet_count'])
    tweets_str = ' '.join(str(x) for x in tweets)
    return tweets_str
    


if __name__ == '__main__':
    tweets_str = scrape_twitter("heat", "nuggets")
    file = open("data/raw/tweets.txt", "w")
    file.write(tweets_str)
    file.close()
    # tweets_df['content'].to_string(file, index_names=False)
    # print(tweets_df['content'].to_json())
