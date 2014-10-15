from node import Node

class Stack(object):

	def __init__(self):
		self.top = None
		self.size = 0
	def push(self, data):
		newitem = Node(data)
		newitem.next = self.top
		self.top = newitem
		self.size += 1
	def pop(self):
		if self.top is None:
			raise TypeError("Nothing in the stack")
		self.size -= 1
		temp = self.top.data
		self.top = self.top.next
		return temp