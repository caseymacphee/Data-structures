from node import Node

class Queue:
	def __init__(self):
		self.head = None
		self.size = 0

	def dequeue(self):
		if self.head is None:
			raise ValueError
		elif self.head.next is None:
			dequeued = self.head
			self.head = None
			self.size -=1
			return dequeued.data
		else:
			current = self.head
			while current.next is not None and current.next.next is not None:
				current = current.next
			self.tail = current
			dequeued = current.next
			current.next = None
			self.size -= 1
			return dequeued.data
	
	def enqueue(self, val):
		enqueued = Node(val)
		self.size += 1
		if self.head is None:
			self.head = enqueued
		else:
			enqueued.next = self.head
			self.head = enqueued



