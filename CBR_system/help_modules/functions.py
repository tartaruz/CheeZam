def caseFromQuery(cbr):
    track_id, track = cbr.spotify.search(cbr.query, cbr.artist, 'track')

    while not track:
        print(f"Could not find any results for {cbr.query}. Try again")
        cbr.setQuery()
        track_id, track = cbr.spotify.search(cbr.query, cbr.artist, 'track')

    try:
        cbr.artist_genres = cbr.spotify.getArtistGenres(track['album']['artists'][0]['id'])
    except:
        pass

    audio_features = cbr.spotify.getAudioFeatures(track_id).json()
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
    # print(track_features["track_id"],track_features["track_name"], " by ", track_features["track_artist"])
    new_case = list(map(lambda x: x[1], track_features.items()))
   
    return new_case