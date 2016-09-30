import tweepy
consumer_key = 'uEiVjyO98GwtHeV84vnxFb8YI'
consumer_secret = '2HUukAwVgr3X4nworgMnvNDQT2vy4QNObmztx9Q3thvHPn2hJI'
access_token = 	'378220962-KJNvdtMLLKz4gEDEc9eAS7KdJUPFWsRQDDVYJH98'
access_token_secret = 'a78VF2709JZghNQWd11rskIfuTshKVanDbGz9W8f6egyI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

myStream.filter(track=['python'])
# for tweet in public_tweets:
    # print tweet.text.encode('utf-8')


# user = api.get_user('geczy')
# print user.screen_name
#
#
# # streaming api
# class MyStreamListener(tweepy.StreamListener):
#
#     def on_data(self, data):
#         print data
#         return True
#     def on_error(self, status):
#         print status
#
#
# twitterStream = Stream(auth, listener())
# twitterStream.filter(track=["order"])
