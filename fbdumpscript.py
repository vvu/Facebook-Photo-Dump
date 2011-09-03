import urllib2
import json

APP_ID= '221362074553481'
REDIRECT_URI='http://localhost:3000'

authorize_url = "https://graph.facebook.com/oauth/authorize?type=user_agent&client_id={0}&redirect_uri={1}&scope=user_photos" .format ( APP_ID, REDIRECT_URI)

print 'Please visit this url to get the access token:' +  authorize_url

accesstoken = raw_input ("Enter Access Token:")

print 'Making request, please wait'

request_url= "https://graph.facebook.com/me/photos?access_token={0}&limit=100000&fields=source".format(accesstoken)

try:
    fbresponse = urllib2.urlopen(request_url)
except e:
    print "Stuff went wrong. Error was:{0}".format(e)
fbjson= fbresponse.read()

sourcesraw=json.loads(fbjson)

print sourcesraw
print sourcesraw['data']
