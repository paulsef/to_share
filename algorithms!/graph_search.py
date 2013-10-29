import pandas as pd
import example_graph
import pdb
import copy


class Vertex:
	"""
	a node has attribute edges which is a list of all the 
	nodes that node points to. If weighted, each outnode will be a tuple
	containing the name of the outnode and it's weight. Directionality will
	be represented by having the outnode point to the innode and visa versa
	"""
	def __init__(self,name,edges, weights):
		self.name = name
		self.edges = edges
		self.weights = weights
		self.visited = False

class Search:
	'''
	A search class takes as input a starting node,the name of an ending node, and
	a python Queue objec. It has method visit() which traverses the graph searching
	for the ending node name by whatever means are associated with the Queue object
	'''
	def __init__(self,start, end_name, fringe):
		self.start = start
		self.end_name = end_name
		self.fringe = fringe

	def visit(self):
		visited = []
		self.fringe.put((0,self.start, []))
		while not self.fringe.empty():
			new = self.fringe.get()
			old_weight = new[0]
			new_node = new[1]
			path = new[2]
			if new_node.visited:
				continue
			new_node.visited = True
			visited.append(new_node)
			if new_node.name == self.end_name:
				path.append(new_node)
				return path
			for i in range(len(new_node.edges)):
				edge = new_node.edges[i]
				path_copy = copy.copy(path)
				path_copy.append(new_node)
				weight = new_node.weights[i] + old_weight
				self.fringe.put((weight, edge, path_copy))
		return 'end point was not found'
			



def adj_matrix(neighborhood):
	'''
	creates an adjacency matrix from a list of Vertex objects
	'''
	names = [vert.name for vert in neighborhood]
	matrix = pd.DataFrame(index = names, columns = names).fillna(0)
	for vertex in neighborhood:
		print str(j) + ' htis is ih'
		for i in range(len(vertex.edges)):
			edge = vertex.edges[i]
			weight = vertex.weights[i]
			matrix.loc[vertex.name, edge.name] = weight
	return matrix

def dfs(starting_node, neighborhood = None):
	# perform a depth-first search of the space, returns a list of
	# nodes that were hit in the search from starting node
	if not starting_node.visited:
		for edge in starting_node.edges:
			starting_node.visited = True
			dfs(edge, node_name)
	if neighborhood:
		hit = [vert if vert.visited == True else None for vert in neighborhood]
		nothit = [vert if vert.visited == False else None for vert in neighborhood]
		return hit, nothit


def reset(neighborhood):
	'''
	resets visited flags to False
	'''
	for i in neighborhood:
		i.visited = False
	return neighborhood


		
if __name__ == '__main__':
	print adj_matrix(create_neighborhood)
		
