from node import Node

class Linked_list(object):


	def __init__(self, node = None):
		
		if type(node) != Node and node is not None:
			raise TypeError('Object passed in must be of type Node')

		self.front = node
		if node is not None:
			self.size = 1
		else:
			self.size = 0


	def __str__(self):
		
		current = self.front
		if self.front is None:
			return "()"
		elif self.front.next is None:
			return "(" + str(self.front.data) + ")"
		else:	
			string = "("
			string += str(current.data)
			while current.next is not None:
				string +=  ", " + str(current.next.data)
				current = current.next
			string += ")"
			return string


	def __iter__(self):
		self.current = self.front
		return self

	def next(self):

		if self.current is None:
			raise StopIteration
		else:
			temp = self.current.data
			self.current = self.current.next
			return temp

	def __add__(self, other):

		i = self.__iter__()
		j = other.__iter__()
		newlist = Linked_list()
		for val in i:
			newlist.append(val)
		for val in j:
			newlist.append(val)
		newlist.size = self.size + other.size
		return newlist

	def append(self, val):

		current = self.front
		other = Node(val)
		
		if self.front is None:
			self.front = other
			self.size += 1

		else:
			while current.next is not None:
				current = current.next
			current.next = other
			self.size += 1


	def remove(self, value):

		current = self.front
		if self.front.data == value:
			self.front = self.front.next
		else:
			while current.next.data != value and current.next is not None:
				current = current.next
			if current.next.data == value:
				current.next = current.next.next
				self.size -= 1

	
	def search(self, value):

		current = self.front

		if self.front.data == value:
			return self.front
		while current.next is not None and current.next.data != value:
			current = current.next
		if current.next is None:
			return None
		else:
			return current.next


	def insert(self, val):

		node = Node(val)
		node.next = self.front
		self.front = node
		self.size += 1


	def pop(self):

		current = self.front.data
		self.front = self.front.next
		self.size -= 1
		return current


	def size(self):

		return self.size


	def join(self, other):

		if type(other) != Linked_list:
			raise TypeError("Object passed in must be of type Linked_list")

		current = self.front

		while current.next is not None:
			current = current.next

		current.next = other.front
		self.size += other.size






