from app import features_collection
from dTree import dTree
import requests
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
		track = song_data['track']
		artist = song_data['artist']
		response = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist="+artist+"&track="+track+"&api_key="+self.lastfm_api_key+"&format=json")
		print response
