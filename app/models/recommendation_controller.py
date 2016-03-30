from app import features_collection
from dTree import dTree
class recommendation:
	def __init__(self):
		self.ml_model = dTree().init(features_collection) 

	def get_rec(self):
		pass
