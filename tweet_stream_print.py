import tweepy

atoken = "852089632703619072-QpbEjNyqkfRdrJHfqOmv4EtZr8e5beo"
asecret = "pdv4NfRAp6KBTGtAJ2SfyuIf3UBef1nqbmAfErLTJ8D0L"
ckey = "ut4Q429ds9CAcCF1o0FN2CqRA"
csecret = "SC27jGlr64h8skUqT6LXoNJFO7ctff5h0oFpzw2h2wYYpeIobM"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

cricTweet = tweepy.Cursor(api.search, q='cricket', geocode="-22.9122,-43.2302,1km").items(10)

for tweet in cricTweet:
   print tweet.created_at, tweet.text, tweet.lang
