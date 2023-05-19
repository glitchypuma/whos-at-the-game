import sys
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
import pandas as pd
from django.http import HttpResponse, JsonResponse
import requests

#snscraper dev version: 0.6.2.20230321.dev12+gea49c19

# Create your views here.
def scrape_twitter(request, away, home):

    
    if(request.method == "GET"):
        print("Good request")
        scraper = sntwitter.TwitterSearchScraper(home + " " + away)

        tweets = []

        for i, tweet in enumerate(scraper.get_items()):
            data = [tweet.date, 
                    tweet.id, 
                    tweet.content, 
                    tweet.user.username, 
                    tweet.likeCount, 
                    tweet.retweetCount
            ]
            tweets.append(data)
            if i > 100:
                break

        tweets_df = pd.DataFrame(tweets, columns=['date', 'id', 'content', 'username', 
                                                    'like_count', 'retweet_count'])
        return JsonResponse(tweets_df.to_json(), safe=False)
    else:
        return HttpResponse(status=400)


# if __name__ == '__main__':
#     scrape_twitter("dodgers", "cardinals")
