from textblob import TextBlobimport tweepy

# Twitter API credentials
consumer_key = '8KcB9TkpRjhWxqBh9eYMx6aBA'
consumer_secret = 'xvZy7Uk7zgR5ZkLq3DyCiPm3q3yHcHc1CqP1oNkH1aOlMnBn1jM2mN1o1kJlHpJjI'
access_token = '1147877573428895744-Aq3T0DGkZCnY novalidtoken'
access_token_secret = 'Ea3RjhWxqBh9eYMx6aBAxvZy7Uk7zgR5ZkLq3DyCiPm3q3yHcHc1CqP1oNkH1aOlMnBn1jM2mN1o1kJlHpJjI'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get the tweets related to a particular stock
tweets = api.search(q='AAPL', lang='en', count=100)

# Analyze the sentiment of the tweets
polarity = 0
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

# Print the average sentiment
print(polarity/len(tweets))
