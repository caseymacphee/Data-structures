class Vertice(object):
 	def __init__(self, data = None):
 		self.data = data
 	def __str__(self):
 		return str(self.data)

class Edge(object):
	def __init__(self, n1, n2):
		self.edge_properties = []
		self.vert1 = n1
		self.vert2 = n2
	def __str__(self):
		return '({}, {})'.format(str(self.vert1.data), str(self.vert2.data))

class Graph(object):
	def __init__(self):
		self.nodes = []
		self.edges = []

	def nodes(self):
		return self.nodes

	def add_node(self, n):
		new_node = Vertice(n)
		self.nodes.append(new_node)

	def add_edge(self, n1, n2):
		new_node1 = Vertice(n1)
		new_node2 = Vertice(n2)
		new_edge = Edge(new_node1, new_node2)
		self.edges.append(new_edge)
		found = False
		for vertice in self.nodes:
			if vertice.data == n1:
				found = True
		if not found:
			self.nodes.append(new_node1)
		found = False
		for vertice in self.nodes:
			if vertice.data == n2:
				found = True
		if not found:
			self.nodes.append(new_node2)

	def del_node(self, n):
		found = False
		for vertice in self.nodes:
			if vertice.data == n:
				found = True
				self.nodes.remove(vertice)
		if found ==False:
			raise Exception("That vertice isn't in the graph")
		
		for edge in self.edges:
			if edge.vert1.data == n or edge.vert2.data == n:
				self.edges.remove(edge)
	
	def del_edge(self, n1, n2):
		found = False
		for edge in self.edges:
			if edge.vert1.data == n1 and edge.vert2.data == n2:
				found = True
				self.edges.remove(edge)
		if found == False:
			raise Exception("That edge isn't in the graph")

	def has_node(self, n):
		for vertice in self.nodes:
			if vertice.data == n:
				return True
		return False

	def neighbors(self, n):
		neighbor_list = []
		for edge in self.edges:
			if edge.vert1.data == n:
				neighbor_list.append(edge.vert2.data)
			if edge.vert2.data == n:
				neighbor_list.append(edge.vert1.data)
		return neighbor_list

	def adjacent(self, n1, n2):
		n1_neighbors = self.neighbors(n1)
		if n2 in n1_neighbors:
			return True
		else:
			return False



