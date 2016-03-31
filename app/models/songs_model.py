from app import db
class songs:
	def __init__(self):
		self.attributes = ['song_id','artist','song','uri']
		self.database = 'musicon'
		self.collection = 'songs'

	def get(self,ids):
		print "fetching songs with ids",ids
		ids = [int(i) for i in ids]
		cursor_object  = db[self.database][self.collection].find({"song_id":{"$in":ids}})
		uris = list()
		for doc in cursor_object:
			uris.append(doc['uri'])
		return uris
