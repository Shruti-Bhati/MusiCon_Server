from user_model import user as user_model
class user:
	def __init__(self):
		self.user_model_object = user_model()
		self.attributes = self.user_model_object.attributes

	def create(self,options):
		userdata = self.get(options)
		if len(userdata):
			raise Exception("Username already exists",400)
		else:
			response = self.user_model_object.create(options)
			return response

	def get(self,options):
		username = options['username']
		if not username or len(username) == 0:
			raise Exception("Username not given",400)
		userdata = self.user_model_object.get({"username":username})
		return userdata

	def update_state(self,options):
		if '_id' not in options or 'update_type' not in options:
			raise Exception("No id given for user",400)
		# else:
			# update_type
		pass
