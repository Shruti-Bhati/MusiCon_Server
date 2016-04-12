import requests,json,urllib
class spotify:
	def __init__(self):
		self.endpoint = "https://api.spotify.com/v1/search"

	def get_uris(self,songs):
		uris = []
		for song_obj in songs:
			track = urllib.quote_plus(song_obj['track'])
			artist = urllib.quote_plus(song_obj['artist'])
			response = requests.get(self.endpoint + "?q=" + track + ":" + artist + "&type=track,artist&limit=1")
			response = response.json()
			if len(response['tracks']['items']):
				track_uri = response['tracks']['items'][0]['uri']
				uris.append(track_uri)
		print uris
		return uris