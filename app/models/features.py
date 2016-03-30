from app import db
class features:
	def __init__(self):
		self.attributes = ['id','value']
		self.database = 'musicon'
		self.collections = ['event_feature','location_feature','mood_feature','weather_feature']

	def getall(self):
		print "fetching all attributes"
		collections_data = {}
		for collection in self.collections:
			cursor_object =  db[self.database][collection].find({})
			docs = {}
			for doc in cursor_object:
				docs[doc['value']] = doc['id']
			collections_data[collection] = docs
		return collections_data