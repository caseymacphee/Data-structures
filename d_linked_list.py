from node import Node

class D_linked_list(object):


	def __init__(self):
		self.front = None
		self.tail = None
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


	def append(self, val):
		current = self.front
		other = Node(val)
		self.tail = other
		if self.front is None:
			self.front = other
			self.currentsize += 1

		else:
			while current.next is not None:
				current = current.next
			current.next = other
			other.prev = current
			self.currentsize += 1


	def remove(self, node):
		if type(node) != Node:
			raise Exception('Method takes only objects of type Node')
		found = False
		value = node.data
		if self.front is None:
			return None
		else:
			if self.front.data == value:
				self.front = self.front.next
				self.currentsize -=1
				if self.front is not None:
					self.front.prev = None
					if self.front.next is None:
						self.tail = self.front
			else:
				current = self.front
				while current.next is not None:
					if current.next.data == value:
						found = True
						current.next = current.next.next
						if current.next is not None:
							current.next.prev = current
						else:
							self.tail = current
						self.currentsize -= 1
						break
					current = current.next
				if current.next == None and found == False:
					return None


	def insert(self, val):
		node = Node(val)
		node.next = self.front
		if self.front is None:
			self.tail = node
		self.front = node
		if self.front.next is not None:
			self.front.next.prev = self.front
		self.currentsize += 1


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
				self.front = None
				self.tail = None
			self.currentsize -= 1
			return temp.data


	def pop(self):
		if self.front is not None:
			current = self.front.data
			self.front = self.front.next
			if self.front is not None:
				self.front.prev = None
			else:
				self.tail = self.front
			self.currentsize -= 1
			return current
		else:
			return None


	def size(self):
		return self.currentsize

# insert(val) will insert the value 'val' at the head of the list
# append(val) will append the value 'val' at the tail of the list
# pop() will pop the first value off the head of the list and return it.
# shift() will remove the last value from the tail of the list and return it.
# remove(val) will remove the first instance of 'val' found in the list, starting from the head. If 'val' is not present, it will raise an appropriate Python exception.







