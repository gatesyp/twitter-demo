import tweepy
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
consumer_key = 'uEiVjyO98GwtHeV84vnxFb8YI'
consumer_secret = '2HUukAwVgr3X4nworgMnvNDQT2vy4QNObmztx9Q3thvHPn2hJI'
access_token = 	'378220962-KJNvdtMLLKz4gEDEc9eAS7KdJUPFWsRQDDVYJH98'
access_token_secret = 'a78VF2709JZghNQWd11rskIfuTshKVanDbGz9W8f6egyI'

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        # print data.__class__
        return True

    def on_error(self, status):
        print status



#This handles Twitter authetification and the connection to Twitter Streaming API
listen = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, listen)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track=['python', 'javascript', 'ruby'])
