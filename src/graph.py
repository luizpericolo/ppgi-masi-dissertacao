import random

class Graph:
	def __init__(self, debug=False):
		self.adjacency = None
		self.nodes = []
		self.edges = []
		self.debug = debug
	
	def check_edge(self, x, y):
		""" Checks wether edge (x, y) or (y, x) already exists. """

		result = (x, y) in self.edges or (y, x) in self.edges

		if self.debug:
			print "Edges ({}, {}) or ({}, {}) in edge list? {}".format(x, y, y, x, result)

		return result
	
	def add_edge(self, x, y):
		""" Adds edge (x, y) to the edge list. """

		if self.debug:
			print "Edge ({}, {}) was added.".format(x, y)

		# Adding the new edge to the edge list.
		self.edges.append((x, y))
		
		# Updating the adjacency matrix.
		self.adjacency[x][y] = 1
		self.adjacency[y][x] = 1

	def add_node(self, x):
		""" Adds node x to the node list. """
		
		if self.debug:
			print "Node {} was added.".format(x)

		# Adding the new node to the node list.
		self.nodes.append(x)

		# Updating the adjacency matrix.	
		self.adjacency[x][x] = 0
			
	def print_adjacency(self):
		""" Pretty prints the adjacency matrix for a graph. """

		for line in self.adjacency:
			print line
		print

	def print_edges(self):
		""" Pretty prints the edge list. """

		print "Edge list:" 
		for edge in self.edges:
			print edge

	def print_nodes(self):
		""" Pretty prints the node list. """

		print "Node list:"

		for node in self.nodes:
			print node

class RandomGraphCreator:
	
	def __init__(self, debug=False):
		self.graph = Graph(debug=debug)

	def create(self, n_nodes):
		self.graph.adjacency = [[ 0 for i in range(n_nodes)] for j in range(n_nodes)]

		for i in range(n_nodes):
			
			# If there are nodes in the node list, we shall randomize
			#	which edges to create
			if self.graph.nodes:
				# The max number of edges we can create is the current number of nodes
				#	the graph has.
				if len(self.graph.nodes) == 1:
					n_edges = 1
				else:
					n_edges = random.randrange(1, len(self.graph.nodes))

				n_edges = 1

				while n_edges:
					target_node = random.randrange(0, len(self.graph.nodes))
					# If an edge between j and target_node does not exist
					#	create it and diminish the amount of edges we must create.
					if not self.graph.check_edge(i, target_node):
						self.graph.add_edge(i, target_node)
						n_edges -= 1
				
			# Adding the new node to the node list.
			self.graph.add_node(i)

		return self.graph


