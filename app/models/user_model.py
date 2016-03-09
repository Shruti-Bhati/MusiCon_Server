from app import db
class user:
	def __init__(self):
		self.compl_attributes = ['username','email','first_name','last_name']
		self.opt_attributes = ['phone']
		self.database = 'musicon'
		self.collection = 'user'
	
	def get(self,options):
		print "Fetching user",options
		cursor_object =  db[self.database][self.collection].find(options)
		docs = list()
		for doc in cursor_object:
			docs.append(doc)
		return docs
		
	def create(self,options):
		print "Creating user",options
		data = {key:options[key] for key in options}
		insert_id = db[self.database][self.collection].insert_one(data).inserted_id
		print 'User inserted id -',insert_id
		return insert_id