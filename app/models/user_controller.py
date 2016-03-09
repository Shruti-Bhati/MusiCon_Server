from user_model import user as user_model
from pam_model import pam as pam_model
from bson.objectid import ObjectId
class user:
	def __init__(self):
		self.user_model_object = user_model()
		self.pam_model = pam_model()
		self.attributes = self.user_model_object.compl_attributes + self.user_model_object.opt_attributes

	def create(self,options):
		userdata = self.get(options)
		if len(userdata):
			raise Exception("Emailid already exists",400)
		else:
			finalData = {}
			errors = list()
			for key in self.attributes:
				if key in self.user_model_object.compl_attributes and key not in options:
					errors.append(key)
				elif key in options:
					finalData[key] = options[key]
			print finalData
			if len(errors):
				print errors
				raise Exception("Following compulsory fields were not given -"+",".join(errors),400)
			response = self.user_model_object.create(finalData)
			return response

	def get(self,options):
		no_email = False
		no_id = False
		no_username = False
		if 'email' not in options or len(options['email']) == 0:
			no_email = True
		if 'user_id' not in options or len(options['user_id']) == 0:
			no_id = True			
		if 'username' not in options or len(options['username']) == 0:
			no_username = True
		print no_email,no_username,no_id
		if no_email and no_id and no_username:
			raise Exception("NO email/id/username was provided",400)
		data = {}

		if 'email' in options and len(options['email']) != 0:
			data['email'] = options['email']
		elif 'user_id' in options and len(options['user_id']) != 0:
			data['_id'] = ObjectId(options['user_id'])
		elif 'username' in options and len(options['username']) != 0:
			data['username'] = options['username']

		userdata = self.user_model_object.get(data)
		beautified_data = {}
		for key in userdata[0]:
			if key == '_id':
				beautified_data['user_id'] = str(userdata[0][key])
			else:
				beautified_data[key] = userdata[0][key]
		return beautified_data

	def update_state(self,options):
		if 'user_id' not in options or 'update_type' not in options:
			raise Exception("No id/update_type given for user",400)
		else:
			if options['update_type'] == "PAM":
				response = self.pam_model.insert(options)
				return response
