from app import db
class songs:
	def __init__(self):
		self.attributes = ['id','artist','song','uri']
		self.database = 'musicon'
		self.collection = 'songs'

	def get(self,ids):
		print "fetching songs with ids",ids
		cursor_object  = db[self.database][self.collection].find({"id":{"$in":ids}})
		uris = list()
		for doc in cursor_object:
			uris.append(doc['uri'])
		return uris