import pdb
import random
import math
import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, cdist, squareform

'''
data should always be passed in as a feature matrix
'''

def initial_centroids(data, k):
	'''
	chooses k random points from the data to use as initial centroids
	returns a list containing the initial centroids
	'''
	# choose a random number using random.sample() (no replacement)
	centroids = random.sample(data, k)
	return np.array(centroids)

def assign(data, centroids, distance_metric):
	'''
	takes data and centroids and assigns the data points to their closest
	centroid. returns closest, a list mapping the corresponding rows to
	to the nearest input vectors
	'''
	# compute which points belong to which centroids using a given
	# distance metric
	distance_mat = cdist(data, centroids, distance_metric)
	closest = np.argmin(distance_mat,1)
	return closest




def update(data, closest):
	'''
	takes data, centroids, and a list which maps the data points to their
	corresponding closest centroids. returns the new centroids which will be
	returned as a list of np vectors that represent the position of the centroid
	'''
	# compute the new poistions for the centroids by minimizing the distance between
	# the centroid and its assigned points
	new_centroids = []
	for k in set(closest):
		mask = k == closest
		subset = data[mask]
		new_centroids.append(np.mean(subset,0))
	return new_centroids


def sse(data, closest, final_centroid, distance_metric):
 	'''
	computes the sum squared error, the distance of each point to
	its final centroid, sqaured, and summed over all data points
	'''
	final_centroid_array = np.array(final_centroid)
	squared_distances = []
	# iterate through the number of rows
	for i in range(len(data)):
		# get the closest centroid that corresponds to the current row
		index = closest[i]
		a = data[i]
		b = final_centroid[index]
		dist_squared = pdist([a,b],distance_metric)**2
		squared_distances.append(dist_squared)
	return sum(squared_distances)
		
		



def execute_k_means(data, k, distance_metric):
	first_centroids = initial_centroids(data, k)
	i = 0
	while i < 10:
		print "this is iteration " + str(i)
		print 'let\'s find the closest centroids...'
		assignment = assign(data, first_centroids, distance_metric)
		print 'got em! let\'s give em a new home...'
		new_centroids = update(data, assignment)
		print 'the centroids seem happy, let\'s check...'
		new_assignment = assign(data, new_centroids, distance_metric)
		print 'k we have the new asignementds...'
		if ((assignment == new_assignment).all()):
			print 'you won!'
			return new_assignment, new_centroids
		else:
			print 'one more time...'
			i += 1
			first_centroids = new_centroids
	return new_assignment, new_centroids 


