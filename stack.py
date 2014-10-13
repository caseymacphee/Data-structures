from node import Node

class Stack(object):

	def __init__(self):
		self.top = None

	def push(self, data):
		newitem = Node(data)
		newitem.next = self.top
		self.top = newitem

	def pop(self):
		if self.top is None:
			raise TypeError("Nothing in the stack")
		temp = self.top.data
		self.top = self.top.next
		return temp