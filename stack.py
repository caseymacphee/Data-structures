from node import Node

class Stack(object):

	def __init__(self):
		self.top = None
		self.current_size = 0
	
	def push(self, data):
		new_Node = Node(data)
		new_Node.next = self.top
		self.top = new_Node
		self.current_size += 1
	
	def pop(self):
		if self.top is None:
			raise Exception('There is nothing left in the stack.')
		self.current_size -= 1
		popped_val = self.top.data
		self.top = self.top.next
		return popped_val