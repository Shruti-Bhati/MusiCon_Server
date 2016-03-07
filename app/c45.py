from math import log
from copy import deepcopy
from __future__ import division
import numpy as np
import operator

def entropy(class_vector):
   
    ze=0
    oe=0
    if len(class_vector)==0:
        return 0

    num_samp=len(class_vector)
    zc=0    
    for i in range(num_samp):
        if class_vector[i]==0:
            zc+=1

    one_ratio=num_samp-zc
    one_ratio=float(one_ratio/num_samp)
    zero_ratio=float(zc/num_samp)

    if not one_ratio==0:
        oe=one_ratio*log(one_ratio,2)
    if not zero_ratio==0:
        ze=zero_ratio*log(zero_ratio,2)
    entropy_val = 0-(oe)-(ze)

    return entropy_val
    
    
def information_gain(features, classes ):
    
    thres=ts
    main_entropy=entropy(classes)
    
    num_att=len(features[0][:])
    alpha=[]
    vec_len=len(classes)

    tf=np.array(features) 

    for i in range(num_att):
        zsub_vec=[]
        osub_vec=[]

        if num_att==1:
            att_vect=tf.tolist()
        else:
            att_vect=tf[:,i].tolist()
        
        for j in range(vec_len):
            zc=0
            if att_vect[j]<thres[i]:
                zsub_vec.append(classes[j])
                zc+=1
            else:
                osub_vec.append(classes[j])
                
        one_ratio=(vec_len-zc)/vec_len
        zero_ratio=zc/vec_len
        alpha.append(main_entropy-one_ratio*entropy(osub_vec)-zero_ratio*entropy(zsub_vec))

    return alpha             
            
            
    
class DecisionTree():

    def __init__(self, depth_limit=float("inf")):
        self.root = None
        self.depth_limit = depth_limit
        self.nodes=[]
        self.ids=[]
        self.thrshould= ts

        self.f_1=[]
        self.f_0=[]
        self.c_1=[]
        self.c_0=[]

    def fit(self, features, classes):

        self.root = self.__build_tree__(features, classes,elem=[])

    def __build_tree__(self, features, classes, depth=0,elem=[]):   

        # check if all items in a list is the same 
        def all_same(items):
            return all(x == items[0] for x in items)
        #return the frequent item in a list 
        def most_common(lst):
            return max(set(lst), key=lst.count)
        def compute_att_no(elem):

            ids=deepcopy(self.ids)

            for i in range(len(elem)-1):
                ids.pop(elem[i])

            return ids.pop(elem[-1])

        def new_fet_class(features,classes,Best_alpha,att_no,val):
            new_feeatures=[]
            new_classes=[]
            for i in range(len(classes)):
                if val==0:
                    if features[i][Best_alpha]<self.thrshould[att_no]:
                        new_feeatures.append(features[i][:])
                        new_classes.append(classes[i])
                else:
                    if features[i][Best_alpha]>=self.thrshould[att_no]:
                        new_feeatures.append(features[i][:])
                        new_classes.append(classes[i])

            [r.pop(Best_alpha) for r in new_feeatures]       

            return new_feeatures,new_classes
        
        
        #set indices
        
  
        
        if depth == self.depth_limit:

            return DecisionNode(None,None,None,class_label=most_common(classes))
        if  classes==[]:

            return DecisionNode(None,None,None,class_label=1)
        if  features==[]:

            return DecisionNode(None,None,None,class_label=most_common(classes))
        # check for base cases 
        if all_same(classes):

            return DecisionNode(None,None,None,class_label=classes[0])
        if depth ==0:

            for i in range(0,len(features[0])):
                self.ids.append(i)
      
        # compute information gain for every feature alpha 
        while not depth==self.depth_limit :

            if len(elem)==len(self.ids):

                return DecisionNode(None,None,None,class_label=most_common(classes))


            alphas=information_gain(features, classes )

            if alphas==[]:

                return DecisionNode(None,None,None,class_label=most_common(classes))

            index, value = max(enumerate(alphas), key=operator.itemgetter(1))
            Best_alpha =index

            elem=elem[0:len(alphas)-1]
            elem.append(Best_alpha)
            

            att_no=compute_att_no(elem)

            features_1,classes_1=new_fet_class(features,classes,Best_alpha,att_no,1)
            features_0,classes_0=new_fet_class(features,classes,Best_alpha,att_no,0)
            self.f_1.append((features_1))
            self.f_0.append((features_0))
            self.c_1.append((classes_1))
            self.c_0.append((classes_0))
           
            sf1=self.f_1.pop()
           
            left_node=self.__build_tree__(sf1,self.c_1.pop(),depth+1,elem)

            sf0=self.f_0.pop();

            right_node=self.__build_tree__(sf0,self.c_0.pop(),depth+1,elem[:-1])

            new_node=DecisionNode(left_node,right_node,decision_function=lambda feature:feature[att_no])
            if depth==0:
                self.root=new_node
            
            return new_node

            
           
        

    ########################Classification method #########################################       
    def classify(self, features):

       
        bin_features=[]
        for test in (features):
            nf_vec=[]
            c=0
            for e in test:
                if e<self.thrshould[c]:
                    nf_vec.append(0)
                else:
                    nf_vec.append(1)
                c+=1
            bin_features.append(nf_vec)
                    

        classifier_output = [self.root.decide(example) for example in bin_features]
        return classifier_output


