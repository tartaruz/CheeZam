import requests

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

    def search(self, query, qtype):
        url = f'https://api.spotify.com/v1/search'
        params = {
            'query': query.replace(' ', '+'),
            'type': qtype,
            'limit': 1,
            'market': 'NO'
        }

        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

        return requests.get(url, params=params, headers=headers)

    def getAudioFeatures(self, searchResponse):
        track_id = searchResponse.json()['tracks']['items'][0]['id']
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