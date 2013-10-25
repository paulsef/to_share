# An object oriented approach to implentning the multi-armed bandit and ucb1 AB testing
# algorithms. The 'buttons' can be though of as the machine in a multi-armed bandit case
from random import choice
from random import random
import pymc as mc
import math
import pdb


class Buttons:
	"""
	The button class has attributes reward_count, trial_count, big_n, and name. The name
	attribute should be passed in as a string
	"""
	def __init__(self, name):
		self.reward_count = 1.0
		self.trial_count= 1.0
		self.big_n = 1.0
		self.name = name


	def get_reward(self, reward=None):
		"""
		Takes as input a choice corresponding to a button name that represents the 
		"lever" we have chosen to pull. Reward is an integer that will be added to that
		buttons running reward. The trial count is then updated. If no reward is 
		passed, the function returns the current running reward.
		"""
		if reward != None:
			self.reward_count += reward
			self.trial_count += 1
		else:
		 	return self.reward_count


def choose(buttons, data, algorithm, threshold = .10):
	"""
	takes as input an iterable of button types and input data. Currently the data will be passed in the form of 
	a dictionary with button names as keys and boolean lists from a bernoulli distribution as
	values. Optionally, set the threshold for the espilon first algorithm.
	For ucb1 returns a list of length three with name, best_true_mean, and confidence_bound.
	For epsilon first returns a list of length two with name and current expected mean
	"""
	# Exploration
	rand = random()
	if (rand < threshold) and (algorithm != 'ucb1'):
		# if we decided to explore, choose a button at random
		r_choice = choice(buttons)
		# determing the reward for the choice and update reward
		r_choice.reward_count += choice(data[r_choice.name])
		r_choice.trial_count += 1
		return [r_choice, r_choice.reward_count/r_choice.trial_count]
	# if we're not in ucb1 and we're not exploring, find the max expected mean
	expected_list = []
	for i in range(len(buttons)):
		if algorithm == 'ucb1':
			confidence_bound = math.sqrt(2*math.log(buttons[i].big_n)/buttons[i].trial_count)
			best_true_mean = (buttons[i].reward_count/buttons[i].trial_count) + confidence_bound
			# update the expected list
			expected_list.append([buttons[i], best_true_mean, confidence_bound])
			buttons[i].big_n += 1
			#print buttons[i], buttons[i].big_n, buttons[i].name
		else:
			# calculate expected mean and update to expected list
			expected_list.append([buttons[i],buttons[i].reward_count/buttons[i].trial_count])
	# get maximum expected value (adjusted with conf. bound for ucb1)
	winner = max(expected_list, key = lambda x: x[1])
	# update the reward and trial counts
	winner[0].get_reward(choice(data[winner[0].name]))
	return winner 



