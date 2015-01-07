import webapp2
import logging

import json
import sys
import tweepy
import calendar
import ConfigParser
import HTMLParser

from tweepy import *
from ConfigParser import NoSectionError, NoOptionError
from time import gmtime, strftime
from urllib2 import urlopen, URLError
from zlib import decompress, MAX_WBITS

from google.appengine.ext import ndb
from google.appengine.ext import db

import pprint

HOURS = 0.01
USER_ID = 1288 # Your Stack Overflow user id for sharing links
MAX_TWEET_LEN = 140
DATE_FORMAT = "%Y %b %d %H:%M:%S UTC"

class LastTweet(ndb.Model):
    since_id = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class Hero(db.Model):
    id = db.IntegerProperty()
    handle = db.StringProperty()
    score = db.FloatProperty()
    date = db.DateTimeProperty(auto_now_add=True)


# Finds tweets containing #ActsOfSuperness and scores them by retweets
# Modifies player in datastore and potentially @replies that tweet 
# to tell them that they have become a stronger superhero
#
# Author: Will McFadden
#
# Dependencies: tweepy (https://github.com/tweepy/tweepy)
#               Twitter API: https://dev.twitter.com/
class TweetSuper(webapp2.RequestHandler):
    def get(self):
        # Get UTC time now and 8 hours ago.
        # to_time = calendar.timegm(gmtime())
#         self.response.write('Time Now: ' + strftime(DATE_FORMAT, gmtime(to_time)) + '<br/>')
#         from_time = to_time - (HOURS * 60 * 60)
# 
#         from_time_displ = strftime(DATE_FORMAT, gmtime(from_time))
#         to_time_displ = strftime(DATE_FORMAT, gmtime(to_time))
#         window_msg = 'Target Window: ' + from_time_displ + ' to ' + to_time_displ
#         self.response.write(window_msg + '<br/>')
#         self.response.write('<br/>')

        try:
            config = ConfigParser.RawConfigParser()
            config.read('settings.cfg')
    
            CONSUMER_KEY = config.get('Twitter OAuth', 'CONSUMER_KEY')
            CONSUMER_SECRET = config.get('Twitter OAuth', 'CONSUMER_SECRET')
            ACCESS_TOKEN_KEY = config.get('Twitter OAuth', 'ACCESS_TOKEN_KEY')
            ACCESS_TOKEN_SECRET = config.get('Twitter OAuth', 'ACCESS_TOKEN_SECRET')

            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth)      
            
            
            
            sid_query = LastTweet.query().order(-LastTweet.since_id)
            sids = sid_query.fetch(1)
            if(len(sids)>0):
                sid = sids[0].since_id
                tweet = sids[0]
            else:
                sid = 552808969216200704
                tweet = LastTweet()
            
            found = api.search('%23ActsOfSuperness',since_id=sid)
#             self.response.write('found '+str(len(found))+'<br />')
            for f in found:
                if hasattr(f, 'retweeted_status'):
                    ff = f.retweeted_status
                    id2 = ff.user.id
                    name2 = ff.user.screen_name
                    hero = Hero.all().filter('id =', id2).fetch(10)
                    if(len(hero)>1):
                        for i in range(1,len(hero)):
                            hero[0].score=hero[0].score+hero[i].score
                        db.delete(hero[1:])
                    hero = Hero.all().filter('id =', id2).get()
                    points = 10.0/(ff.user.followers+1.0)
                    hero.score = hero.score+points
                    hero.put()
#                     self.response.write(ff.user.screen_name+' got: '+str(points)+' points<br />')
                name = f.user.screen_name
                id = f.user.id
                hero = Hero.all().filter('id =', id).fetch(10)
                if len(hero)>0:
                    if(len(hero)>1):
                        for i in range(1,len(hero)):
                            hero[0].score=hero[0].score+hero[i].score
                        db.delete(hero[1:])
                    hero = hero[0]
                    points = 1.0
                    hero.score = hero.score+points
                    hero.put()
                else:
                    hero = Hero()
                    hero.id = id
                    hero.handle = name
                    hero.score = 1.0
                    hero.put()
#                 self.response.write(f.user.screen_name+' got: '+str(1)+' points.  Total score: ' +str(hero.score)+' <br />')
            
            if(len(found)>0):
                status = found[0].text
                new_sid = found[0].id
                tweet.since_id=new_sid
                tweet.put()
                
#                 self.response.write(status)
                api.update_status(status)
        except TweepError:
            logging.error('TweepError: ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1]))
            logging.error(status)
        except URLError:
            logging.error('URLError: ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1]))
            logging.error(status)
        except:
            logging.error('Unexpected error: ' + str(sys.exc_info()[0]) + str(sys.exc_info()[1]))      
            

app = webapp2.WSGIApplication([
    ('/tweet_super', TweetSuper)
], debug=False)
