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
		cursor_object = db[self.database][self.collection].find({"username":username,"feature":feature}).sort([("timestamp",-1)]).limit(1)
		feature_id = 0
		for doc in cursor_object:
			feature_id = doc['feature_id']
			break
		feature_id = int(feature_id)
		print feature_id
		for key in features_collection[feature]:
			if features_collection[feature][key] == feature_id:
				return key

			

	def insert(self,options):
		print "Updating pam state for user ",options['username']
		if "feature_id" in options:
			options["feature_id"] = int(options["feature_id"]) + 1
		data = {key:options[key] for key in options}
		data['timestamp'] = time.time()
		insert_id = db[self.database][self.collection].insert_one(data).inserted_id
		return insert_id