from Queue import Queue
from Queue import PriorityQueue

class Vertice(object):
 	def __init__(self, data = None):
 		self.data = data
 		self.visited = False
 		self.directed = False

 	def __str__(self):
 		return str(self.data)

class Edge(object):
	def __init__(self, n1, n2, weight = None):
		self.edge_properties = []
		self.weight = weight
		self.vert1 = n1
		self.vert2 = n2
	def __str__(self):
		return '({}, {}, {})'.format(str(self.vert1.data), str(self.vert2.data), str(self.weight))

class Graph(object):
	def __init__(self):
		self.nodes = []
		self.edges = []

	def nodes(self):
		return self.nodes

	def add_node(self, n):
		new_node = Vertice(n)
		self.nodes.append(new_node)

	def return_node(self, n):
		for node in self.nodes:
			if node.data == n:
				return node

	def edge_weight(self, n1, n2):
		for edge in self.edges:
			if edge.vert1.data == n1 and edge.vert2.data == n2:
				return edge.weight
			if edge.vert1.data == n2 and edge.vert2.data == n1:
				return edge.weight
		return None

	def add_edge(self, n1, n2, weight = None):
		found = False
		for vertice in self.nodes:
			if vertice.data == n1:
				found = True
				node1 = vertice
		if not found:
			node1 = Vertice(n1)
			self.nodes.append(node1)
		found = False
		for vertice in self.nodes:
			if vertice.data == n2:
				found = True
				node2 = vertice
		if not found:
			node2 = Vertice(n2)
			self.nodes.append(node2)
		for edge in self.edges:
			if edge.vert1.data == n1 and edge.vert2.data == n2:
				raise Exception('Cannot duplicate edges')
		new_edge = Edge(node1, node2, weight)
		self.edges.append(new_edge)
		

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
				neighbor_list.append(edge.vert2)
			if edge.vert2.data == n:
				neighbor_list.append(edge.vert1)
		return neighbor_list

	def adjacent(self, n1, n2):
		n1_neighbors = self.neighbors(n1)
		for node in n1_neighbors:
			if node.data == n2:
				return True
		return False

	def depth_traversal(self, n):
		found = False
		visited_path = []
		for node in self.nodes:
			node.visited = False
			if node.data == n:
				found = True
				start_node = node
		if found:
			self._depth_traversal(start_node, visited_path)
			return visited_path
		else:
			raise Exception("That node doesn't appear to be in the graph")

	def _depth_traversal(self, n, path):
		n.visited = True
		path.append(n.data)
		for node in self.neighbors(n.data):
			if node.visited == False:
				self._depth_traversal(node, path)

	def breadth_traversal(self, n):
		found = False
		path = []
		for node in self.nodes:
			node.visited = False
			if node.data == n:
				found = True
				start_node = node
		if not found:
			raise Exception("That node doesn't appear to be in the graph")
		else:
			queue = Queue()
			start_node.visited = True
			path.append(start_node.data)
			queue.put(start_node)
			while queue.qsize() > 0:
				first_in = queue.get()
				for node in self.neighbors(first_in.data):
					if node.visited == False:
						path.append(node.data)
						node.visited = True
						queue.put(node)
		return path
	
	def dijkstra_algorithm(self, start_node, target):
		min_path = PriorityQueue()
		best_answer = -1
		for node in self.nodes:
			node.visited = False
			if node.data == start_node:
				found = True
				current = node
		if not found:
			raise Exception("The start node doesn't appear to be in the graph")
		for node in self.nodes:
			if node.data == target:
				found = True
				end = node
		if not found:
			raise Exception("That target node doesn't appear to be in the graph")
		min_path.put((0, [current.data]))
		while not min_path.empty():

			shortest = min_path.get()
			current_weight = shortest[0]
			path = shortest[1]
			lastval = path.pop()
			path.append(lastval)
			lastnode = self.return_node(lastval)
			lastnode.visited = True

			for neighbor in self.neighbors(lastval):
				if neighbor.visited == False:
					weight = self.edge_weight(lastval, neighbor.data)
					new_path = path[:]
					new_path.append(neighbor.data)
					new_min = current_weight + weight
					if neighbor == end:
						if best_answer == -1 or best_answer >= new_min:
							best_answer = new_min
							yield (new_min, new_path)
					min_path.put((new_min, new_path))







