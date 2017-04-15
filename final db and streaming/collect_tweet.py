from __future__ import print_function
import tweepy
import json
import MySQLdb
from dateutil import parser
 
WORDS = ['a']


ACCESS_TOKEN = "852089632703619072-QpbEjNyqkfRdrJHfqOmv4EtZr8e5beo"
ACCESS_TOKEN_SECRET = "pdv4NfRAp6KBTGtAJ2SfyuIf3UBef1nqbmAfErLTJ8D0L"
CONSUMER_KEY = "ut4Q429ds9CAcCF1o0FN2CqRA"
CONSUMER_SECRET = "SC27jGlr64h8skUqT6LXoNJFO7ctff5h0oFpzw2h2wYYpeIobM"

HOST = "localhost"
USER = "testuser"
PASSWD = "password"
DATABASE = "testdb"
 
# This function takes the 'created_at', 'text', 'screen_name' and 'tweet_id' and stores it
# into a MySQL database
def store_data_tweets(tweet_id, tweet_text, created_at, retweet_count, user_id, screen_name, name):
    db=MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE, charset="utf8")
    cursor = db.cursor()

#insert into tweets
    insert_query = "INSERT INTO tweets (tweet_id, tweet_text, created_at, retweet_count, user_id, screen_name, name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (tweet_id, tweet_text, created_at, retweet_count, user_id, screen_name, name))
    db.commit()
    cursor.close()
    db.close()
    return

def store_data_users(user_id,screen_name,name,location,url,description,created_at,followers_count,friends_count):
    db=MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DATABASE, charset="utf8")
    cursor = db.cursor()

#insert into users
    insert_query = "INSERT INTO users (user_id,screen_name,name,location,url,description,created_at,followers_count,friends_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (user_id,screen_name,name,location,url,description,created_at,followers_count,friends_count))
    db.commit()
    cursor.close()
    db.close()
    return
 
class StreamListener(tweepy.StreamListener):    
    #This is a class provided by tweepy to access the Twitter Streaming API.
 
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
    def on_data(self, data):
        #This is the meat of the script...it connects to your mysql database and stores the tweet
        try:
           # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #grab the wanted data from the Tweet ---> tweets
            tweet_text = datajson['text']
            screen_name = datajson['user']['screen_name']
            tweet_id = datajson['id']
            created_at = parser.parse(datajson['created_at'])
            retweet_count = datajson['retweet_count']
            name = datajson['user']['name']
            user_id = datajson['user']['id_str']         
            
            #insert the data into tweets table of db
            store_data_tweets(tweet_id, tweet_text, created_at, retweet_count, user_id, screen_name, name)
            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            
            #grab the wanted data from the Tweet ---> users
            user_id = datajson['user']['id_str']
            screen_name =  datajson['user']['screen_name']
            name = datajson['user']['name']
            location = datajson['user']['location']
            url = datajson['user']['url']
            description = datajson['user']['description']
            created_at = parser.parse(datajson['user']['created_at'])
            followers_count = datajson['user']['followers_count']
            friends_count = datajson['user']['friends_count']

            store_data_users(user_id,screen_name,name,location,url,description,created_at,followers_count,friends_count)
            print("user info collected")

        except Exception as e:
           print(e)
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
