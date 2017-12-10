#import the necessary methods from tweepy library
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


#Variables that contains the user credentials to access Twitter API
access_token = 	"921747026475446272-i60skcWVYVvkxyzOmwwWwHTWCeGXFBJ"
access_token_secret = "MtXIe2Bk3SJrE7qYAetSzJvDrZvwYCc9s99LPhy0uOLt4"
consumer_key = 	"rngnf5OS0rt4TGONL2RGQxCCE"
consumer_secret = "YqOENirRbcRIl7dUUWPTgASgyh2FLYLd28Z6iAnYNtfEdDsUnW"

#This is a basic listener that just prints recieved tweets to stdout
class StdOutListener(StreamListener):

    def on_data(self, data):
            print (data)
            return True

    def on_error(self, status):
            print (status)

if __name__ == '__main__':

    #this handles Twitter authentification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'basketball', 'soccer', 'football'
    #it's possible to filter by any key word
    stream.filter(track=['basketball', 'soccer', 'football'])
