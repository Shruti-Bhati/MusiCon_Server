from model import user as user_model
class user:
	def __init__(self):
		self.user_model_object = user_model()

	def create(self,options):
		username = options['username']
		if not username or len(username) == 0:
			raise Exception("Username not given",400)
		userdata = self.user_model_object.get({"username":username})
		if len(userdata):
			raise Exception("Username already exists",400)
		else:
			response = self.user_model_object.create(options)
			return response

	def get(self,options):
		pass

	def update_state(self,options):
		pass
