import billboard
import requests
from pprint import pprint
import re
from datetime import datetime, timedelta
import pickle

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from multiprocessing import Pool

# define spotify auth

spotify_auth = {
    'client_id':'4ea6e458711041f38a00cb6c72d32d8f',
    'client_secret': 'a69b5cccf41c434da8a2d1d3aa839e44'
}

def get_spotify_track(title, artist, spotify_auth):
    '''
    a function that takes a track and artist as string arguments
    alongside a spotify_auth object with client_id ans client_secret
    and returns the spotify track:uri and track:popularity
    '''
    
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=spotify_auth['client_id'], 
        client_secret=spotify_auth['client_secret']
    ))
    
    results = sp.search(q=f'{title} {artist}', type="track", limit=1)
    # this loop feels unecessary
    for idx, track in enumerate(results['tracks']['items']):
        obj = { 'uri':track['uri'], 'popularity':track['popularity'] }
        return obj

def get_conception_date(date):
    '''
    a function that takes a date_str yyyy-mm-dd
    and returns a date_str yyyy-mm-dd
    for the date 270 days prior
    '''
    
    date = datetime.strptime(date, "%Y-%m-%d").date()
    conception_date = date - timedelta(days=270)
    date_str = datetime.strftime(conception_date, "%Y-%m-%d")
    return date_str

def get_conception_date_tracks(date):
    mixtape_len = 10
    '''
    a function to return a cc2000 object for site utlity
    
    function takes:
        - a date_str yyyy-mm-dd
        - a mixtape_len
        
    and returns the indexed billboard top-100 track playing 270 days before the input date
    '''
    
    # validate date
    if not re.search("\d\d\d\d-\d\d-\d\d", date):
        print('incorrect date format')
        return
    
    # get conception date
    # conception_date = get_conception_date(date)
    # date = conception_date
    
    
    # get hot 100 chart for date
    try:
        chart = billboard.ChartData('hot-100', date=date)
        # chart = chart[0:mixtape_len]

    except:
        print('chart error')
        return
    
    if not chart:
        return # return if no chart object
    
    tracks = []
    i = 0
    spicy = mixtape_len
    num_tracks = 0
    
    while num_tracks < mixtape_len:
        # print(num_tracks)
        try:
            track = {}
            track['title'] = chart[i].title
            track['artist'] = chart[i].artist
            track['spicy'] = spicy

            track_spotify_data = get_spotify_track(chart[i].title, chart[i].artist, spotify_auth)
            track['spotify_uri'] = track_spotify_data['uri']
            track['popularity'] = track_spotify_data['popularity']

            tracks.append(track)
            i+=1
            spicy -= 1
            num_tracks += 1
            
        except:
            i+=1
            pass # pass if spotify can't find track, still build list of 10/mixtape_len tracks
    
    return tracks


"""
def make_cc2000_data():
    '''
    makes the output dictionary for cc2000
    starts from current date and works backwards to 1958-08-04
    returns object with dates yyyy-mm-dd as keys
    '''
    
    cc2000_data = {}
    
    end_date_str = '1958-08-04' # this is the day the first billboard hot 100 was released
    # end_date_str = '2022-02-24' # this is a closer test date
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    
    date = datetime.today().date()
    
    date = datetime.strptime('2022-04-30', "%Y-%m-%d").date()
    
    while date >= end_date: # end once billboard runs out of data
   
        date_str = datetime.strftime(date, "%Y-%m-%d")
        day_object = get_conception_date_tracks(date_str, 10)
        
        cc2000_data[date_str] = day_object

        try:
           print(date, day_object[0]['title'], day_object[0]['artist'])
        except:
          print(date + ' error')
        
        # decrease by one day
        date -= timedelta(days = 7)
    
    return cc2000_data
"""


def make_dates(start_date):
    '''
    makes the dates for cc2000
    starts from the start date and works backwards to 1958-08-04
    '''
    
    dates = []
    
    end_date_str = '1958-08-04' # this is the day the first billboard hot 100 was released
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    date = datetime.strptime(start_date, "%Y-%m-%d").date()
    
    while date >= end_date: # end once billboard runs out of data

        date_str = datetime.strftime(date, "%Y-%m-%d")
        
        dates.append(date_str)
        
        # decrease by one day
        date -= timedelta(days = 1)
    
    return dates

dates = make_dates('2022-05-01')

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(2) as p:
        print(p.map(get_conception_date_tracks, dates))