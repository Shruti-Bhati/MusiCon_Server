from app import features_collection
from dTree import dTree
class recommendation:
	def __init__(self):
		self.ml_model = dTree().init(features_collection) 
		self.ml_model.load_traningDB('Sample_Data.csv')
		self.ml_model.train()

	def get_rec(self,state):
		return self.ml_model.test(state)