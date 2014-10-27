from node import Node

class Linked_list(object):
	def __init__(self):
		self.front = None
		self.currentsize = 0

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
		newlist.currentsize = self.currentsize + other.currentsize
		return newlist

	def append(self, val):
		current = self.front
		other = Node(val)
		self.currentsize += 1
		if self.front is None:
			self.front = other
		else:
			while current.next is not None:
				current = current.next
			current.next = other

	def remove(self, node):
		if self.front is not None:
			current = self.front
			value = node.data
			if self.front.data == value:
				self.front = self.front.next
				self.currentsize -= 1
			else:
				while current.next is not None:
					prev = current
					current = current.next
					if current.data == value:
						prev.next = current.next
						self.currentsize -=1

	def search(self, value):
		if self.front is None:
			return None
		current = self.front
		if current.data == value:
			return current
		while current.next is not None:
			current = current.next
			if current.data == value:
				return current
		return None

	def insert(self, val):
		node = Node(val)
		node.next = self.front
		self.front = node
		self.currentsize += 1

	def pop(self):
		if self.front is None:
			return None
		current = self.front.data
		self.front = self.front.next
		self.currentsize -= 1
		return current

	def size(self):
		return self.currentsize

	def join(self, other):
		if type(other) != Linked_list:
			raise TypeError("Object passed in must be of type Linked_list")
		current = self.front
		while current.next is not None:
			current = current.next
		current.next = other.front
		self.currentsize += other.currentsize


