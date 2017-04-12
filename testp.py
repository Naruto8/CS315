import tweepy

from pymongo import MongoClient

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import urllib3.contrib.pyopenssl

# urllib3.contrib.pyopenssl.inject_into_urllib3()
KEYWORDS = ['India', 'Football', 'IIT Kanpur']

access_token = "852089632703619072-QpbEjNyqkfRdrJHfqOmv4EtZr8e5beo"
access_token_secret = "pdv4NfRAp6KBTGtAJ2SfyuIf3UBef1nqbmAfErLTJ8D0L"
consumer_key = "ut4Q429ds9CAcCF1o0FN2CqRA"
consumer_secret = "SC27jGlr64h8skUqT6LXoNJFO7ctff5h0oFpzw2h2wYYpeIobM"

class StdOutListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        created_at = tweet["created_at"]
        id_str = tweet["id_str"]
        text = tweet["text"]
        obj = {"created_at":created_at, "id_str":id_str, "text":text,}
        tweetind = collection.insert_one(obj).inserted_id
        print(obj)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    listen = StdOutListener()
    stream = Stream(auth, listen)

    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.test_database
    collection = db.test_collection

    stream.filter(track=KEYWORDS)
