from flask import Flask
import flask_restful
import feedparser as fp
import requests as req
import tweepy as tp

myApp = Flask(__name__)
myApi = flask_restful.Api(myApp)

#This is built with a single user in mind. 
class tweeter(flask_restful.Resource):

    @myApp.route('/tweeter/<key>')
    def get(key):
        checkClass = TweetProcess()
        return {'resultCode': str(checkClass.startVet(str(key)))}

    @myApp.errorhandler(500)
    def internal_err(error):
        return {'resultCode':"Backend Error"}

myApi.add_resource(tweeter, '/<key>')


class TweetProcess:

    def startVet(self, k):
        
        #A hashed version of the key. I called this API such that the key got hashed on client side. 
        myhash = ""  #Insert a string you want to act as a key
        if str(k) == myhash:
            sum, uri_One, img_uri = self.getRssFeed()
            rescode, uri_Two = self.shortenLink(uri_One)
            mainTweet = self.Framer(sum, uri_Two)
            final_res = self.Tweeter(mainTweet)
            if final_res==200:
                return "Success"
            else:
                return "Twitter Error"
        else:
            return "Authentication Error"

    def getRssFeed(self):

        #link to your blog's RSS feed.
        rsslink = "https://yourdomain/blog-feed.xml"    #Replace 'yourdomain' with your website's domain. for e.g: www.mywixblog.com
        RssObject = fp.parse(rsslink)

        try:
            summary = str(RssObject.entries[0].summary)
        except Exception as e:
            summary = "New Featured Article!"

        try:
            url = RssObject.entries[0].link
        except Exception as e:
            url = "https://yourdomain"        #Enter the domain here as well

        try:
            img = RssObject.entries[0].links[1].get('href')
        except Exception as e:
            img = ''


        return summary, url, img
			
			

    def Framer(self, textSummary, shortlink):
        tweet = textSummary + "\n" + str(shortlink)

        return tweet

    def Tweeter(self, text):

        code = 000
				
				#Obtain the following four values from your twitter developer console. Read README.md for help
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_secret = ""

        # authorisation handler using tweepy's built in methods
        authInstance = tp.OAuthHandler(consumer_key, consumer_secret)
        authInstance.set_access_token(access_token, access_secret)

        # calling api
        apiInstance = tp.API(authInstance)

        # tweeting
        try:
            apiInstance.update_status(text)
            code = 200
        except Exception as e:
            code = 500

        return code
