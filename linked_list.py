from node import Node

class Linked_list(object):
	def __init__(self):
		self.front = None
		self.current_size = 0

	def __str__(self):
		current = self.front
		if self.front is None:
			return "()"
		elif self.front.next is None:
			return "(" + str(self.front.data) + ")"
		else:	
			to_string = "("
			to_string += str(current.data)
			while current.next is not None:
				to_string +=  ", " + str(current.next.data)
				current = current.next
			to_string += ")"
			return to_string

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
		first_list_itr = self.__iter__()
		second_list_itr = other.__iter__()
		new_list = Linked_list()
		for val in first_list_itr:
			new_list.append(val)
		for val in second_list_itr:
			new_list.append(val)
		new_list.current_size = self.current_size + other.current_size
		return new_list

	def append(self, val):
		current = self.front
		other = Node(val)
		self.current_size += 1
		if self.front is None:
			self.front = other
		else:
			while current.next is not None:
				current = current.next
			current.next = other

	def remove(self, node):
		if type(node) != Node:
			raise TypeError("Remove takes a Node object")
		if self.front is not None:
			current = self.front
			value = node.data
			if self.front.data == value:
				self.front = self.front.next
				self.current_size -= 1
			else:
				while current.next is not None:
					prev = current
					current = current.next
					if current.data == value:
						prev.next = current.next
						self.current_size -=1

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
		new_node = Node(val)
		new_node.next = self.front
		self.front = new_node
		self.current_size += 1

	def pop(self):
		if self.front is None:
			return None
		current = self.front.data
		self.front = self.front.next
		self.current_size -= 1
		return current

	def size(self):
		return self.current_size

	def join(self, other):
		if type(other) != Linked_list:
			raise TypeError("Object passed in must be of type Linked_list")
		current = self.front
		while current.next is not None:
			current = current.next
		current.next = other.front
		self.current_size += other.current_size


