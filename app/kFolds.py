from math import floor

ts= [0]*4
import numpy as np
def load_csv(data_file_path, class_index=-1):
    handle = open(data_file_path, 'r')
    contents = handle.read()
    handle.close()
    rows = contents.split('\n')
    out = np.array([  [float(i) for i in r.split(',')] for r in rows if r ])
    classes= list(map(int,  out[:, class_index]))
    features = out[:, :class_index]
    return features, classes

def generate_k_folds(dataset, k):
    
    # where each fold is a tuple like (training_set, test_set)
    # where each set is a tuple like (examples, classes)
    features=dataset[0]
    classes=dataset[1]

    list_folds=[];
    sub_siz=int(floor(len(classes)/k))
    for i in (range(0,len(classes)-sub_siz+1,sub_siz)):

        f=[]
        cs=[]
        fs=[]
        f=np.array(deepcopy(features))
        cs=deepcopy(classes)
        fs=f.tolist()

        start=i
        end= i+sub_siz
        
        
        test_set=[]
        test_examples=[]
        test_calsses=[]
        test_examples=fs[start:end][:]

        test_calsses=cs[start:end]

        for j in range(start,end):
            fs.pop([start][0]) 
            cs.pop(start)

     
        test_set=(test_examples,test_calsses)
        train_set=(fs,cs)
        list_folds.append((train_set,test_set))

    return list_folds
