from server.DB import DbConnector
from Retrieval import Retrieval
from Reuse import Reuse
from Spotify import Spotify
from model.case import case

class CBR:
    def __init__(self):
        self.DB = DbConnector()
        self.r1 = Retrieval(self.DB)
        self.r2 = Reuse()
        self.spotify = Spotify()
        self.query = None
        self.case = None

    def setQuery(self):
        self.query = input('Please input a song title and artist (Song title Artist name) to predict genre: ').lower()

    def caseFromQuery(self):
        track = self.spotify.search(self.query, 'track')
        audio_features = self.spotify.getAudioFeatures(track).json()
        track = track.json()['tracks']['items'][0]
        track_features = {
            'index': None,
            'track_id': track['id'],
            'track_name': track['name'],
            'track_artist': track['artists'][0]['name'],
            'track_popularity': track['popularity'],
            'track_album_id': track['album']['id'],
            'track_album_name': track['album']['name'],
            'track_album_release_date': track['album']['release_date'],
            'playlist_name': None,
            'playlist_id': None,
            'playlist_genre': None,
            'playlist_subgenre': None,
            'danceability': audio_features['danceability'],
            'energy': audio_features['energy'],
            'key_value': audio_features['key'],
            'loudness': audio_features['loudness'],
            'mode': audio_features['mode'],
            'speechiness': audio_features['speechiness'],
            'acousticness': audio_features['acousticness'],
            'instrumentalness': audio_features['instrumentalness'],
            'liveness': audio_features['liveness'],
            'valence': audio_features['valence'],
            'tempo': audio_features['tempo'],
            'duration_ms': audio_features['duration_ms']
        }
        new_case = list(map(lambda x: x[1], track_features.items()))
        self.case = case(new_case)

def main():
    cbr = CBR()
    cbr.setQuery()
    cbr.caseFromQuery()
    print(cbr.case)

if __name__ == '__main__':
    main()