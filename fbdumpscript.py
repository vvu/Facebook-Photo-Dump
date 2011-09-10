import urllib2
import json
import os
APP_ID= '221362074553481' #FaceBook App ID
REDIRECT_URI='http://localhost:3000' #Callback URL

authorize_url = "https://graph.facebook.com/oauth/authorize?type=user_agent&client_id={0}&redirect_uri={1}&scope=user_photos" .format ( APP_ID, REDIRECT_URI)

print 'Facebook Photo Dump by Victor Vu. This is licensed under the Apache 2.0 License.\n\nPlease visit this url to get the access token:\n' +  authorize_url

accesstoken = raw_input ("Enter Access Token:")

print 'Making request, please wait'

request_url= "https://graph.facebook.com/me/photos?access_token={0}&limit=100000&fields=source".format(accesstoken)


#try to connect to fb, catch any errors while connecting
#TODO:Implement FB Exceptions
try:
    fbresponse = urllib2.urlopen(request_url)
except e:
    print "Stuff went wrong. Error was:{0}".format(e)
fbjson= fbresponse.read()

sourcesraw=json.loads(fbjson)

print "Found {0} photos. Beginning download.".format(len(sourcesraw['data']))

os.mkdir('facebookphotos')

length= len(sourcesraw['data'])
count= 1

#Loops through list of photos and downloads them to a folder locally
for e in sourcesraw['data']:
    print "Downloading {0} of {1}.".format(count, length)
    psource= e['source']
    response=urllib2.urlopen(psource)
    rawjpeg=response.read()
    f = open('facebookphotos/{0}.jpg'.format(e['id']), "w")
    f.write(rawjpeg)
    f.close()
    count=count+1

print ('Finished downloading all photos! They can be found in the same directory as this script.')

