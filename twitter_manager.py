from tweepy.streaming import StreamListener, json
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
ckey= 'rlee33vXmHIlmR5tQljIX0ucD'
csecret= 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
atoken= '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
asecret= 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'


class twtmanager(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        decoded = json.loads(data)
        txt = decoded['text']
        # screenName = decoded["screen_name"]
        # name= decoded["name"]
        # hashTag = decoded["hashtag"]
        # createdAt = decoded["created_at"]
        # print(hashTag)
        if "the" in txt:
            self.sendTweet("test")
        print("\n" + txt)
        return True


    def on_error(self, status):
        print(status)

    def sendTweet(self, text):
        # api.update_status("@" + usr + " " + text)
        print "demo!"
        # print ("@" + usr + " " + text)
        print text
        return


if __name__ == '__main__':
    l = twtmanager()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    stream = Stream(auth, l)
    stream.filter(track=['@DunSuciRun'])

