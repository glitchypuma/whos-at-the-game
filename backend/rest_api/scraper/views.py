import sys
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter
import pandas as pd
import os

# Create your views here.
def scrape_twitter(home_team, away_team):
    scraper = sntwitter.TwitterSearchScraper(home_team + " " + away_team)

    tweets = []

    for i, tweet in enumerate(scraper.get_items()):
        data = [tweet.date, 
                tweet.id, 
                tweet.content, 
                tweet.user.username, 
                tweet.likeCount, 
                tweet.retweetcount
        ]
        tweets.append(data)
        if i > 10:
            break

    tweets_df = pd.DataFrame(tweets, columns=['date', 'id', 'content', 'username', 
                                                'like_count', 'retweet_count'])
    print(tweets_df.to_string)


if __name__ == '__main__':
    scrape_twitter("lakers", "nuggets")
