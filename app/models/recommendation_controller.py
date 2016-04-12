from app import features_collection
from dTree import dTree
import requests,json,urllib
class recommendation:
	def __init__(self):
		self.ml_model = dTree()
		self.ml_model.init(features_collection) 
		self.ml_model.load_traningDB('Sample_Data.csv')
		self.ml_model.train()
		self.lastfm_api_key = "46dd0949a4bd4e2c4c9c679797ac9dd3"

	def get_rec(self,state):
		return self.ml_model.test(state)

	def get_similar_tracks(self,song_data,num):
		similar = []
		track = urllib.quote_plus(song_data[0]['track'])
		artist = urllib.quote_plus(song_data[0]['artist'])
		response = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist="+artist+"&track="+track+"&api_key="+self.lastfm_api_key+"&format=json")
		response = response.json()
		tracks = response['similartracks']['track']
		if len(tracks):
			print "found similar tracks"
			filtered_tracks = tracks[:num]
			filtered_tracks = [{"track":a['name'],"artist":a['artist']['name']} for a in filtered_tracks]
			similar = filtered_tracks
		else:
			print "No similar tracks found,getting similar artists"
			artist_response = requests.get("http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist="+artist+"&api_key="+self.lastfm_api_key+"&format=json")
			artist_response = artist_response.json()
			artists = artist_response['similarartists']['artist']
			if len(artists):
				if len(artists) < num:
					num = len(artists)
				artist_names = []
				for i in range(num):
					sim_artist = artists[i]['name']
					artist_names.append(sim_artist)
				print "Similar artists",artist_names
				similar = self.get_artist_song(artist_names)
		return similar

	def get_artist_song(self,artists):
		artist_song_data = []
		for a in artists:
			a = urllib.quote_plus(a)
			top_tracks_response = requests.get("http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist="+a+"&api_key="+self.lastfm_api_key+"&format=json")
			top_tracks_response = top_tracks_response.json()
			tracks = top_tracks_response['toptracks']['track'][0]
			artist_song_data.append({"artist":tracks['artist']['name'],"track":tracks['name']})	
		return artist_song_data
