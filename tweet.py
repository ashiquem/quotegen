import config
import tweepy
import datetime

with open('quotes.txt','r') as f:
    data = f.readlines()

keys = []
texts = []

for q in data:
    keys.append(q.split('~')[0])
    texts.append(q.split('~')[1].split('\n')[0])

data = dict(zip(keys,texts))    
current_date = str(datetime.datetime.now())[5:10]
status = data[current_date]

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

update = api.update_status(status)
