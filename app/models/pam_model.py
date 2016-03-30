from app import db,features_collection
print features_collection
import time
class pam:
	def __init__(self):
		self.attributes = ['user_id','timestamp','mood_id']
		self.database = 'musicon'
		self.collection = 'pam'
	
	def get(self,options):
		print "Fetching pam data for user",options.user_id
		cursor_object =  db[self.database][self.collection].find({"user_id":options.user_id})
		docs = list()
		for doc in cursor_object:
			docs.append(doc)
		return docs

	def insert(self,options):
		print "Updating pam state for user ",options['user_id']
		data = {key:options[key] for key in options}
		data['timestamp'] = time.time()
		insert_id = db[self.database][self.collection].insert_one(data).inserted_id
		return insert_id