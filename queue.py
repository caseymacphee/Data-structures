from node import Node

class Queue:
	def __init__(self):
		self.head = None
		self.current_size = 0

	def dequeue(self):
		if self.head is None:
			raise ValueError('Nothing to dequeue')
		elif self.head.next is None:
			first_in = self.head
			self.head = None
			self.current_size -=1
			return first_in.data
		else:
			current = self.head
			while current.next is not None and current.next.next is not None:
				current = current.next
			self.tail = current
			first_in = current.next
			current.next = None
			self.current_size -= 1
			return first_in.data
	
	def enqueue(self, val):
		new_node = Node(val)
		self.current_size += 1
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head = new_node

	def size(self):
		return self.current_size



