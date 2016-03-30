#!/usr/bin/python
#import dt lib and others
from sklearn import tree
import csv
import numpy as np

# descission tree class
class dTree():
# intialize 
    def init(self, features):
	self.features=[]
	self.labels=[]
	self.codedFeatures=[]
	self.clf = tree.DecisionTreeClassifier()
	self.sample=[]
#look upi table for all possible values for features needed for coding 
	print features.event_feature.values()
	self.lut_mood=['-','happy','romantic','relaxed','happy','excited','upbeat','happy','confident','calm','sad','frustrated','sleepy']
	self.lut_location=['-','restaurant','home','gym','work']
	self.lut_weather=['-','sunny','breezy','cloudy','rainy','windy']
	self.lut_event=['-','party','driving','running','studying','work','dinner']


#load traning data from csv file
    def load_traningDB(self, file_name):
	data_buff=[]
	with open(file_name, 'rb') as csvfile:
            dataBase = csv.reader(csvfile, delimiter=',')
	    for row in dataBase:
                data_buff.append(row)
	data=np.array(data_buff)
	data_buff=[]
	self.features= data[1:,1:]

	self.labels= data[1:,0]
	



# code data for features 
    def code_data(self):

	self.codedFeatures=np.zeros((len(self.features), len (self.features[0,:])))
#mood
	for cnt,mood in enumerate(self.features[:,0]):
		self.codedFeatures[cnt,0]=self.lut_mood.index(mood)
#location
	for cnt,mood in enumerate(self.features[:,1]):
		self.codedFeatures[cnt,1]=self.lut_location.index(mood)
#weather
	for cnt,mood in enumerate(self.features[:,2]):
		self.codedFeatures[cnt,2]=self.lut_weather.index(mood)
#event
	for cnt,mood in enumerate(self.features[:,3]):
		self.codedFeatures[cnt,3]=self.lut_event.index(mood)


    def code_sample(self,samp):
	
	self.sample=[0,0,0,0]
#mood
	
	self.sample[0]=self.lut_mood.index(samp[0])
#location
	self.sample[1]=self.lut_location.index(samp[1])
	
#weather
	self.sample[2]=self.lut_weather.index(samp[2])	

#event
	self.sample[3]=self.lut_event.index(samp[3])	
#train
    def train(self):
	self.code_data()
	self.clf = self.clf.fit(self.codedFeatures, self.labels)
#test
    def test(self,sample):
	self.code_sample(sample)
	test=np.asarray(self.sample)
	return self.clf.predict(test.reshape(1,-1))
        
def main():

     tree=dTree()
     tree.init()
     tree.load_traningDB('Sample_Data.csv')
     tree.train()
     print "testing sample",['happy', 'home', 'sunny', 'party']
     print tree.test(['happy', 'home', 'sunny', 'party'])
	
   

if __name__ == "__main__":
    main()
