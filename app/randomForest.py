import random
import pickle
def ideal_parameters():
    ideal_depth_limit=10
    ideal_esr=0.75
    ideal_asr=0.75
    return ideal_depth_limit, ideal_esr, ideal_asr

ts= [0]*4

class RandomForest():
    def __init__(self, num_trees, depth_limit, example_subsample_rate, attr_subsample_rate):
        self.trees = []
        self.num_trees = num_trees
        self.depth_limit = depth_limit
        self.example_subsample_rate = example_subsample_rate
        self.attr_subsample_rate = attr_subsample_rate

    def fit(self, features, classes):

        def column(matrix, i):
            return [row[i] for row in matrix]

        f= np.array(features)
        c=np.array(classes)

        fc=np.append(f, c[np.newaxis, :].T, axis=1)
        list_fc=fc.tolist()

        num_att=len(features[0][:])
        train_fc=[]
        self.trees =[None]*self.num_trees
        for i in range(self.num_trees):
            train_fc=[]
            for j in range(int(self.example_subsample_rate*len(features))):
                train_fc.append(random.choice(list_fc))


            tfc=np.array(train_fc)
            sample_len=len(train_fc)
            k =int(self.attr_subsample_rate*num_att)
            selec_att=random.sample(range(num_att), k) 
            train_f=np.empty([sample_len, 0])
            selec_att.sort()
           
            for n in range(len(selec_att)):
                temp=np.array(column(train_fc, selec_att[n]))

                train_f=np.append(train_f, temp[np.newaxis, :].T, axis=1)


            test_classes=column(train_fc,-1)
            train_features=train_f.tolist() 

            self.trees [i]= DecisionTree(depth_limit=self.depth_limit )
            self.trees[i].fit( train_features, test_classes)


        
    def classify(self, features):

        def all_same(items):
            return all(x == items[0] for x in items)
        def most_common(lst):
            return max(set(lst), key=lst.count)
        def column(matrix, i):
            return [row[i] for row in matrix]
        

        output= [None]*self.num_trees
        for i in range(self.num_trees):
            output [i]= self.trees[i].classify(features) 

        final=[]
        for j in range(len(output[0])):

            final.append(most_common(column(output, j)))
        return final



