from datetime import datetime
from random import choice

import tweepy

from config import *
from invisibles import *

def run():
    print("Running repetition-bot.py at", str(datetime.now()))
    tweetQuote()
    print("Finished.")

def tweetQuote():

    # authenticate and set up the Twitter bot
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        twitter = tweepy.API(auth)
    except Exception as e:
        print("Error authenticating with Twitter:",e)

    # generate the tweet text, containing a novel invisible string each time
    # this must be inserted in the middle, since Twitter trims invisibles from the end before posting
    tweet_text = "“What would life be without repetition?”\n"
    tweet_text += generateNonIdentity()
    tweet_text += "\n— Søren Kierkegaard"
    
    try:
        twitter.update_status(status=tweet_text)
        print("Tweet sent successfully!")
    except Exception as e:
        print("Error posting tweet:",e)

# 14^20 possible empty strings ought to be enough
# we want short-ish strings so as not to add an extra line
def generateNonIdentity():
    empty_string = ""
    for i in range(20):
        empty_string += choice(list(invisible_characters.values()))
    return(empty_string)

run()