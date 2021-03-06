
import warnings
warnings.filterwarnings("ignore")
import sys
import numpy as np
from numpy import std,mean
from scipy.io.arff import loadarff as la
from sklearn import svm
from sklearn import datasets
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.tree import DecisionTreeClassifier as DTC


data = la(sys.argv[1])
### get all features
# from itertools import combinations as comb

# features=list(data[1])[:-1]
# features = ["DME_MCTTKAGG","DECOD_Motif2_8","DME_TGAGGTCW","DME_TRKGTGTT","Weeder_2","Improbizer_CTTTCACCTATAATTCCACC","DME_GGCTSWAG","DME_TTWTTYAMWR"]
features = ["Improbizer_GAGGCCCGCGTTCTGCG","DME_CACYYTGRGM","Improbizer_TGTTACAGTATCT","Improbizer_TCCAACATAAATATTT","AAAAWTAYMMAAAT_14","DME_AGMWYTKTGG","Homer_12_5"]

# only consider maximal 15 subset

def calculate_SE_SP_ACC(y_pred,y_true,wrt=1):
	# print "y_pred",y_pred
	# print "y_true",y_true
	
	# PSO3 are 1
	#print y_pred,y_true
	tp = 0.0
	tn = 0.0
	correct = 0.0
	if len(y_pred) != len(y_true):
		print "len(y_pred) != len(y_true)!"
		exit()
	for i in range(len(y_pred)):
		if y_pred[i] == y_true[i]:
			if y_pred[i] == wrt:
				tp += 1
			else:
				tn += 1
			correct += 1
	total = len(y_true)
	T = y_true.count(wrt)
	N = total - T
	#print T,N,total
	if T == 0:
		
		return [1,tn/N,correct/total,tp,tn]
	if N == 0:
		
		return [tp/T,1,correct/total,tp,tn]
	#print total
	return [tp/T,tn/N,correct/total,tp,tn]

def CV(feature_list):
	X=np.array(map(lambda x:list(x),data[0][feature_list].tolist()))
	Y=np.array(data[0]["Class"])
	#print "Y"
	#print Y
	skf_outer = StratifiedKFold(Y, n_folds=10)
	# skf_outer = StratifiedKFold(Y, n_folds=11)
	tuned_parameters_rf = {'n_estimators': range(20,100,20)}
	#acc_svm=[]
	#acc_rf=[]
	se_array=[]
	sp_array=[]
	acc_array=[]
	tp_array=[]
	tn_array=[]
	for train_index_outer, test_index_outer in skf_outer:
		
		train_y_outer = Y[train_index_outer]
		# size = len(train_y_outer)
		# print size
		train_x_outer = X[train_index_outer]
		test_y_outer = Y[test_index_outer]
		test_x_outer = X[test_index_outer]
		size = len(test_y_outer)
		if size == 0:
			continue
		#if len(test_y_outer) == 0:
		#	continue
		# svm_clf = GridSearchCV(SVC(), tuned_parameters_svm, score_func=accuracy_score ,cv=10)
		rf_clf = GridSearchCV(RFC(), tuned_parameters_rf)
		# dt_clf = GridSearchCV(DTC(criterion='entropy'), tuned_parameters_dt)
		# dt_clf = GridSearchCV(DTC(criterion='entropy'), tuned_parameters_dt, score_func=accuracy_score, cv=6)
		#dt_clf = DTC(criterion='entropy',max_depth=2)
		# svm_clf.fit(train_x_outer, train_y_outer)
		#rf_clf.fit(train_x_outer, train_y_outer)
		#print "train_x_outer"
		#print train_x_outer
		# dt_clf=DTC(criterion='entropy',max_depth=2)
		rf_clf.fit(train_x_outer, train_y_outer)
		#print dt_clf.tree_
		#out = dt_clf.export_graphviz(clf, out_file=out)
		#print out.getvalue()
		#tree.export_graphviz(dt_clf,out_file='tree.dot') 
		#exit()
		# y_true_svm, y_pred_svm = test_y_outer, svm_clf.predict(test_x_outer)
		#y_true_rf, y_pred_rf = test_y_outer, rf_clf.predict(test_x_outer)
		y_true_dt, y_pred_dt = test_y_outer, rf_clf.predict(test_x_outer)
		#print "y_pred_dt" 
		#print y_pred_dt
		#acc_svm.append(accuracy_score(y_true_svm, y_pred_svm))
		#acc_rf.append(accuracy_score(y_true_rf, y_pred_rf))
		# [se,sp,acc,tp,tn] = calculate_SE_SP_ACC(map(lambda x:int(x),list(y_pred_svm)),map(lambda x:int(x),list(y_true_svm)))
		[se,sp,acc,tp,tn] = calculate_SE_SP_ACC(map(lambda x:int(x),list(y_pred_dt)),map(lambda x:int(x),list(y_true_dt)))
		# sdf = calculate_SE_SP_ACC(map(lambda x:int(x),list(y_pred_dt)),map(lambda x:int(x),list(y_true_dt)))
		# print sdf
		# se = sdf[0]
		se_array.append(se)
		sp_array.append(sp)
		acc_array.append(acc)
		tp_array.append(tp)
		tn_array.append(tn)
		

	return mean(acc_array)

# a = features[0]
# f=open("peptides_combine_cv.result","wb")
# for i in range(1,len(features)):
# temp = [a,features[i]]
#print temp
iter = 10
accuracy = map(lambda x:CV(features),range(iter))
print accuracy
# c = CV(features)
#print c
# print >>f,",".join(temp),"\t",c[0],"\t",c[1],"\t",c[2],"\t",c[3],"\t",c[4]
print mean(accuracy)








