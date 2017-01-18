# Last.fm Syncing Tool
import os
import requests
import md5

api_head = 'http://ws.audioscrobbler.com/2.0/'
secret = 'the_secret_sauce'

def authorize(user_token):
    stringToHash = 'api_key' + os.environ['LAST_FM_API'] + 'method' + 'auth.getSession' + 'token' + user_token + secret
    stringToHash = stringToHash.encode('utf8')
    print stringToHash
    requestHash = md5.new(stringToHash).digest()
    params = {'api_key': os.environ['LAST_FM_API'], 'method': 'auth.getSession', 'token': user_token, 'api_sig': requestHash}
    print params
    apiResp = requests.post(api_head, params)
    return apiResp.text

def scrobble(song_name, artist_name):
    apiResp = requests.post('http://ws.audioscrobbler.com/2.0/', {'method': 'track.updateNowPlaying', 'apiKey': os.environ['LAST_FM_API'], 'track': song_name, 'artist': artist_name})
    print apiResp.text
