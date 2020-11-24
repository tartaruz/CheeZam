import requests
from difflib import get_close_matches

class Spotify:

    def __init__(self):
        self.access_token, self.token_type = self.generateAccessToken()
    
    def generateAccessToken(self):
        """
        Generates access_token that are needed for authorization with the spotify API.
        """
        resp = requests.post('https://accounts.spotify.com/api/token', headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic Yjk2MDNlY2EyNzdhNGE1NmIxMDAyYjQ4ODg5YTMzZDc6ZTJhNTEwMGIwYWQ2NGRiODhiOTUyZjFlNWY1MjNlY2Y='
        }, data={
            'grant_type': 'client_credentials',
        })
        return resp.json()['access_token'], resp.json()['token_type']

    def search(self, query, artist, qtype):
        """Searches for a song in the Spotify API and returns the song and song id"""

        url = f'https://api.spotify.com/v1/search'
        params = {
            'query': query.replace(' ', '+'),
            'type': qtype,
            'market': 'NO'
        }

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        res = requests.get(url, params=params, headers=headers).json()

        if 'tracks' not in res.keys():
            # If the track are not found, return False.
            return None, False
        
        # Multiple tracks can have the same name, store all tracks in a variable
        tracks = res['tracks']['items']

        artists = []

        # Get all artists from the retrieved tracks        
        for track in tracks:
            for artist_in_track in track['artists']:
                 artists.append(artist_in_track['name'].lower())
        
        artists = list(set(artists))

        # Correct spelling mistakes in the artist name
        corrected_artist = ''.join(get_close_matches(artist, artists, n=1)).lower()
        if len(corrected_artist) == 0:
            corrected_artist = artists[0]
        

        track_id =  None
        selected_track = None

        # Make sure the song the user searched for are made by the correct artist
        for track in sorted(tracks, key=lambda x: x['album']['release_date']):
            breaked = False
            for artist in track['artists']:
                if artist['name'].lower() == corrected_artist:
                    if query.lower() in track['name'].lower():
                        track_id = track['id']
                        selected_track = track
                        breaked = True
                        break
            if breaked:
                break
        
        # If the artist does not have this song, return False.
        if track_id is None:
            return None, False
        
        # Return the track and its id
        return track_id, track


    def getAudioFeatures(self, track_id):
        """
        Get the track's audio features to be able to predict it's genre
        These audio features are the same as the cases in the case base have
        """
        url = 'https://api.spotify.com/v1/audio-features/' + track_id
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        return requests.get(url, headers=headers)

    def getArtistGenres(self, artist_id):
        """
        Get the genres the requested artist usually makes song in, to present to the user later.
        """
        url = f'https://api.spotify.com/v1/artists/{artist_id}'
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        return requests.get(url, headers=headers).json()['genres']