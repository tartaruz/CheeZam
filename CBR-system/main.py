from server.DB import DbConnector
from Retrieval import Retrieval
from Reuse import Reuse
from Spotify import Spotify
from model.case import case

query = [12029,"7tFiyTwD0nx5a1eklYtX2J","Bohemian Rhapsody - 2011 Mix","Queen",
            75,"6X9k3hSsvQck2OfKYdBbXr","A Night At The Opera (Deluxe Remastered Version)",
            1975-11-21,"Classic Rock Drive","37i9dQZF1DXdOEFt9ZX0dh",
            "rock","classic rock",0.392,0.402,0,-9.961,0,0.0536,0.28800000000000003,
            0,0.243,0.228,143.88299999999998,354320]

class CBR:
    def __init__(self):
        self.DB = DbConnector()
        self.r1 = Retrieval(self.DB)
        self.r2 = Reuse(self.r1.cases)
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
        print(track_features["track_id"],track_features["track_name"], " by ", track_features["track_artist"])
        new_case = list(map(lambda x: x[1], track_features.items()))
        self.case = case(new_case)

    def retrieve(self, k):
        # [2,3,2,3,2,3,23]
        self.r1.queryCase = self.case
        self.r1.knn(k)

    def reuse(self):
        similarCases = self.r1.similarCases
        self.r2.retrieval = self.r1
        self.r2.reuse(similarCases)

    def revision(self):
        pass

    def retain(self):
        pass

def main():
    cbr = CBR()
    cbr.setQuery()
    cbr.caseFromQuery()
    print(cbr.case.returnNumericValue())
    print(list(filter(lambda x: x.track_id == '2XU0oxnq2qxCpomAAuJY8K', cbr.r1.cases))[0].returnNumericValue())
    cbr.retrieve(10)
    print(cbr.r1.similarCases)
    # print(cbr.case)
    
    # CBR = CBR()
    # CBR.retive(query,10)
    # CBR.reuse()
    # print(CBR.r2.predictionCase)

if __name__ == '__main__':
    main()
