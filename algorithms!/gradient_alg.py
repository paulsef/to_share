import pandas as pd
import numpy as np
from scipy.spatial import distance
from sklearn import preprocessing
import pdb

'''
An implenation of gradient descent to caclute a linear regression 
'''

def hypo(flavor):
	'''
	returns the function corresponding to the type of regression
	currently only linear regression is supported
	'''
	if flavor == 'linear':
		return np.dot(x, theta)
	#elif flavor == 'log':
	#
	else:
		raise NameError(str(flavor) + ' is not a correct flavor of regression')


def update(x, y, theta, alpha = 1, hypo = None):
	'''
	gradient decent. takes old theta estimates for a regression line, 
	and alpha parameter as a learning parameter, and a data set as a np
	nd array
	'''
	y_hat = hypo('linear')
	# feature_matrix_to_i = np.power(feature_matrix, np.array(range(feature_matrix.shape[1]))+1)
	# sums = np.array([np.sum((y_hat-y)*x[:,i]) for i in range(x.shape[1])])
	# ^^ accidentally defined matrix multiplcation :-), super slow
	sums = np.dot(x.transpose(), y_hat-y)
	new_theta = theta - (sums*alpha)/x.shape[0]
	delta = distance.pdist(np.array([new_theta,theta]), 'euclidean')
	return new_theta, delta

def rsqaured(x, y, theta, hypo = None):
	'''
	compute r squared
	'''
	#y_hat = hypo(x)
	y_hat = np.dot(x, theta)
	rss = np.sum(np.square((y - y_hat)))
	sst = np.sum(np.square(y - np.mean(y)))
	r_squared = 1 - (rss/sst)
	return r_squared

def run(max_iter, feature_matrix, target, min_delta, flavor = 'linear'):
	'''
	iteratavely estimate the regression line
	'''
	i = 1
	new_theta = np.ones(feature_matrix.shape[1])
	new_alpha = .1 #10000000.0
	while i < max_iter:
		new_theta, delta = update(x = feature_matrix, y = target, theta = new_theta, alpha = new_alpha)#,hypo = hypo_funct)
		#new_alpha = new_alpha/i
		i += 1
		if delta < min_delta:
			print 'converged'
			return new_theta, delta
	print 'max iterations reached'
	return new_theta, delta #hypo function

if __name__ == "__main__":
	raw_data = pd.read_csv('data.csv')
	del raw_data['Unnamed: 10']
	del raw_data['Unnamed: 11']
	data = raw_data.dropna()
	data['b'] = 1
	data = pd.DataFrame(preprocessing.scale(data))
	x = np.array(data.iloc[:,[0,1,2,3,4,5,6,7,10]])
	y1 = np.array(data.iloc[:,8])
	y2 = np.array(data.iloc[:,9])
	thetas = run(max_iter = 1000000, feature_matrix = x, target = y2, min_delta = .0000000001)[0] 
	print thetas
	print rsqaured(x, y1, thetas)