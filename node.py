class Node(object):

	def __init__(self, data = None, next = None, prev = None):
		self.prev = prev
		self.data = data
		self.next = next
	def __str__(self):
		return str(self.data)