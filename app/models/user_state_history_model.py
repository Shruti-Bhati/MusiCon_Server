from app import db,features_collection
import time
class user_state_history:
	def __init__(self):
		self.attributes = ['username','timestamp','feature_id','feature']
		self.database = 'musicon'
		self.collection = 'user_state_history'
	
	def get(self,username):
		print "Fetching pam data for user",username
		cursor_object =  db[self.database][self.collection].find({"username":username})
		docs = list()
		for doc in cursor_object:
			docs.append(doc)
		return docs

	def get_latest(self,username,feature):
		sort = {'timestamp':-1}
		cursor_object = db[self.database][self.collection].find({"username":username,"feature":feature},limit=1)
		for doc in cursor_object:
			for key in features_collection[feature]:
				if features_collection[feature][key] == doc['feature_id']:
					return key

	def insert(self,options):
		print "Updating pam state for user ",options['user_id']
		data = {key:options[key] for key in options}
		data['timestamp'] = time.time()
		insert_id = db[self.database][self.collection].insert_one(data).inserted_id
		return insert_id