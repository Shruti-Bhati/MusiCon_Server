class DecisionNode():

    def __init__(self, left, right, decision_function,class_label=None):
        self.left = left
        self.right = right
        self.decision_function = decision_function
        self.class_label = class_label

    def decide(self, feature):

        if self.class_label==1:

            return self.class_label
        elif self.class_label==0:

            return self.class_label
        else:
            

            return self.left.decide(feature) if self.decision_function(feature) else self.right.decide(feature)

def confusion_matrix(classifier_output, true_labels):
   
    tp=0
    fp=0
    tn=0
    fn=0
    for i in range(0,len(true_labels)):
        if true_labels[i]==1 and classifier_output[i]==1:
            tp+=1
        elif true_labels[i]==1 and classifier_output[i]==0:
            fn+=1
        elif true_labels[i]==0 and classifier_output[i]==0:
            tn+=1
        else:
            fp+=1
    conv_mat=[[tp, fn], [fp, tn]]
    #print conv_mat
    return conv_mat
            

def precision(classifier_output, true_labels):

    results=confusion_matrix(classifier_output, true_labels)
    sum_tp_fp=   results[0][0] + results[1][0]
    if sum_tp_fp==0:
        return 1
    return results[0][0]/ sum_tp_fp
    
def recall(classifier_output, true_labels):
    
    results=confusion_matrix(classifier_output, true_labels)
    sum_tp_fn=results[0][0] + results[0][1]
    if sum_tp_fn==0:
        return 1
    return results[0][0]/ sum_tp_fn
    
def accuracy(classifier_output, true_labels):
    results=[]
    results=confusion_matrix(classifier_output, true_labels)
    total=results[0][0] + results[1][1]+ results[0][1]+ results[1][0]
    true_total=results[0][0]+ results[1][1]
    
    return true_total/ total

##########################################################################

