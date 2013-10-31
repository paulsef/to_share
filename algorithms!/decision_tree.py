import pandas as pd
import numpy as np
import math
import treenode
reload(treenode)
import pdb

'''
A recursive implmentation of a decision tree. The dataset is subset
using split until it contains only a column of one unique target
'''

def split(dataset, outcome, feature_index, value = None, continuous = False, for_maker = False):
	'''
	split the dataset on a feature, returns a subset of the data. If 'value' is passed
	the dataset will also be subset for that particular value (or row) of the feature index
	If continuous is passed, two subsets will be returned, one for each side of the
	boolean operator.
	'''
	# check if we're splitting for a new tree
	if for_maker:
		if continuous:
			#if continous, value will be string with g/le and integer
			if value[0] == 'g':
				mask = dataset.loc[:,feature_index] > value[1]
				subset = dataset.loc[mask,:]
			elif value[0] == 'le':
				mask = dataset.loc[:,feature_index] <= value[1]
				subset = dataset.loc[mask,:]
			else:
				print 'just had do that, huh?'
				return None
		else:
			mask = dataset.loc[:,feature_index] == value
			subset = dataset.loc[mask,:]
		del subset[feature_index]
		return subset

	else:
		if continuous:
			#pdb.set_trace()
			mask = dataset.loc[:,feature_index] > value
			subset1 = dataset.loc[mask,:]
			subset2 = dataset.loc[np.invert(mask),:]
			return subset1,subset2
		else:
			mask = dataset.loc[:,feature_index] == value
			subset = dataset.loc[mask,:]
			del subset[feature_index]
			return subset


def entropy(dataset, outcome):
	'''
	calculte the entropy for a a data set
	'''
	probabilities = []
	for unique_outcome in dataset.loc[:,outcome].unique():
		probability = (np.sum(dataset.loc[:,outcome] == unique_outcome))/float(dataset.shape[0])
		probabilities.append(probability*math.log(probability,2))
	return -sum(probabilities)


def top_info_gain(dataset, outcome):
	'''
	find the feature that gives you the most information gain or, in the case of a 
	continuous variable, the value in the feature that gives the most information
	'''
	# base entropy
	info_gain = {}
	continuous_gain = {}
	base_entropy = entropy(dataset, outcome)
	for feature in dataset.columns:
		continuous = False
		if feature == outcome:
			# if we're looking at our feature variable, move on
			continue
		discrete_entropy = []
		# iterate through each unique value in our feature
		for value in dataset.loc[:,feature].unique():
			if dataset[feature].dtype != (np.dtype('O') and np.dtype('bool')):
				# if we're continuous, set the flag and make the call to split
				continuous = True
				continuous_subset1, continuous_subset2 = split(dataset, outcome, feature, value, continuous)
				# calculate the entrop of both our two subsets
				con_entropy1, con_entropy2 = entropy(continuous_subset1,outcome), entropy(continuous_subset2,outcome)
				# weight the two subsets and add take the sum
				weighted_entropy1 = (continuous_subset1.shape[0]*1.0/dataset.shape[0])*con_entropy1
				weighted_entropy2 = (continuous_subset2.shape[0]*1.0/dataset.shape[0])*con_entropy2
				weighted_sum = weighted_entropy1 + weighted_entropy2
				# compute the information gain for each split. the split that gets the most information
				# will be used to make the split
				continuous_gain[base_entropy - weighted_sum] = value
			else:
				# if we're discrete, just get the subset
				subset = split(dataset, outcome,feature, value)
				# compute the entropy and weight it
				weighted_entropy = (subset.shape[0]*1.0/dataset.shape[0])*entropy(subset, outcome)
				# add the weighted entropy gain to the list
				discrete_entropy.append(weighted_entropy)
		if continuous:
			info_gain[feature] = max(continuous_gain)
		else:
			info_gain[feature] = base_entropy - sum(discrete_entropy)
	
	return max(info_gain, key = info_gain.get), continuous_gain

def make_tree(dataset, outcome):
	'''
	creates a tree using a simple tree object
	'''
	# create a new node instance
	new_node = treenode.TreeNode()
	#if len(dataset.loc[:outcome].unique()) == 1:
	#	return
	# get the feature with highest information gain
	new_node.column, cont_dict = top_info_gain(dataset, outcome)
	# determine if top feature is continuous
	if dataset[new_node.column].dtype != (np.dtype('O') and np.dtype('bool')):
		continuous = True
		split_value = cont_dict[max(cont_dict)]
		new_children = [('g' , split_value), ('le', split_value)]
	else:
		continuous = False
		split_value = None
		new_children = dataset[new_node.column].unique()
		# iterate through the unique values for that feature
	for child in new_children:
		# subset the original data for each child
		# make a recursive call each 'child'
		subset = split(dataset = dataset, outcome = outcome, feature_index = new_node.column,
			value = child, continuous = continuous, for_maker = True) 
		if (len(dataset.loc[:,outcome].unique()) == 1 or dataset.shape[1] ==1):#(subset.shape[1] == 1 or subset.shape[0] == 1 or dataset.shape == subset.shape): #subset.shape[1] == 1 or subset.shape[0] == 0 or
			new_node.leaf = True
			result = list(subset[outcome])
			new_node.classes.append(result)
		else:
			new_node.children[child] = make_tree(subset, outcome)
	return new_node


if __name__ == "__main__":
	data = pd.read_csv('golf.csv', header = None)
	data.columns = ['outlook', 'temperature', 'humidity', 'windy', 'outcome']
	data[['temperature','humidity']] = data[['temperature','humidity']].astype('O')
	print top_info_gain(dataset = data, outcome = 'outcome')

