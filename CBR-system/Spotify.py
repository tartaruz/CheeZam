import requests
from difflib import get_close_matches

class Spotify:

    def __init__(self):
        self.access_token, self.token_type = self.generateAccessToken()
    
    def generateAccessToken(self):
        resp = requests.post('https://accounts.spotify.com/api/token', headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic Yjk2MDNlY2EyNzdhNGE1NmIxMDAyYjQ4ODg5YTMzZDc6ZTJhNTEwMGIwYWQ2NGRiODhiOTUyZjFlNWY1MjNlY2Y='
        }, data={
            'grant_type': 'client_credentials',
        })
        return resp.json()['access_token'], resp.json()['token_type']

    def search(self, query, artist, qtype):
        print(query)
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
            return False
        
        tracks = res['tracks']['items']

        artists = []
        
        for track in tracks:
            for artist_in_track in track['artists']:
                 artists.append(artist_in_track['name'].lower())
        
        artists = list(set(artists))

        corrected_artist = ''.join(get_close_matches(artist, artists, n=1)).lower()

        track_id =  None # list(filter(lambda x: x['atrists']['name'].lower() == atrist and x['name'].lower() == query, tracks))
        selected_track = None

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

        if track_id is None:
            return False
        
        return track_id, track


    def getAudioFeatures(self, track_id):
        url = 'https://api.spotify.com/v1/audio-features/' + track_id
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        return requests.get(url, headers=headers)


# def main():
#     spotify = Spotify()
#     print(spotify.getAudioFeatures(spotify.search('Thriller Michael Jackson', 'track').json()['tracks']['items'][0]['id']))

# if __name__ == '__main__':
#     main()