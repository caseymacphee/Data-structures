from node import Node

class D_linked_list(object):

	def __init__(self):
		self.head = None
		self.tail = None
		self.current_size = 0

	def __str__(self):
		current = self.head
		if self.head is None:
			return "()"
		elif self.head.next is None:
			return "(" + str(self.head.data) + ")"
		else:	
			to_string = "("
			to_string += str(current.data)
			while current.next is not None:
				to_string +=  ", " + str(current.next.data)
				current = current.next
			to_string += ")"
			return to_string

	def append(self, val):
		current = self.head
		new_node = Node(val)
		self.tail = new_node
		if self.head is None:
			self.head = new_node
			self.current_size += 1
		else:
			while current.next is not None:
				current = current.next
			current.next = new_node
			new_node.prev = current
			self.current_size += 1

	def remove(self, node):
		if type(node) != Node:
			raise Exception('Method takes only objects of type Node')
		found = False
		value = node.data
		if self.head is None:
			return None
		else:
			if self.head.data == value:
				self.head = self.head.next
				self.current_size -=1
				if self.head is not None:
					self.head.prev = None
					if self.head.next is None:
						self.tail = self.head
			else:
				current = self.head
				while current.next is not None:
					if current.next.data == value:
						found = True
						current.next = current.next.next
						if current.next is not None:
							current.next.prev = current
						else:
							self.tail = current
						self.current_size -= 1
						break
					current = current.next
				if current.next == None and found == False:
					return None

	def insert(self, val):
		node = Node(val)
		node.next = self.head
		if self.head is None:
			self.tail = node
		self.head = node
		if self.head.next is not None:
			self.head.next.prev = self.head
		self.current_size += 1

	def shift(self):
		if self.tail is None:
			return None
		else:
			temp = self.tail
			current = self.tail.prev
			if current is not None:
				current.next = None
				self.tail = current
			else:
				self.head = None
				self.tail = None
			self.current_size -= 1
			return temp.data

	def pop(self):
		if self.head is not None:
			current = self.head.data
			self.head = self.head.next
			if self.head is not None:
				self.head.prev = None
			else:
				self.tail = self.head
			self.current_size -= 1
			return current
		else:
			return None

	def size(self):
		return self.current_size





