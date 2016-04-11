from app import db
class songs:
	def __init__(self):
		self.attributes = ['song_id','artist','song','uri']
		self.database = 'musicon'
		self.collection = 'songs'

	def get(self,ids):
		print "fetching song URIs for stored song ids"
		ids = [int(i) for i in ids]
		cursor_object  = db[self.database][self.collection].find({"song_id":{"$in":ids}})
		song_data = list()
		for doc in cursor_object:
			song_data.append({artist:doc['artist'],track:doc['song']})
		return uris
