class heap(object):

	def __init__(self):
		self.heap = []
		self.heap.insert(0, None)

	def push(self, val):
		self.heap.append(val)
		index = len(self.heap) + 1
		while val < self.heap[index/2] and self.heap[index/2] is not None:
			print index
			swap = self.heap[index/2]
			self.heap[index] = swap
			self.heap[index/2] = val
			index = index/2

	def pop(self):
		if len(self.heap) == 1:
			return None
		else:
			max = self.heap[1]
			lastelement = self.heap.pop()
			self.heap[1] = lastelement
		index = 1
		while self.heap[index] < self.heap[index*2] or self.heap[index] < self.heap[index*2 +1]:
			current = self.heap[index]
			if self.heap[index*2] > self.heap[index*2 + 1]:
				self.heap[index] = self.heap[index*2]
				self.heap[index*2] = current
				index = index * 2
			else:
				self.heap[index] = self.heap[index*2 + 1]
				self.heap[index*2 + 1] = current
				index = (index * 2) + 1

		return max








# For an additional challenge, implement a heap that can be either and allow the choice to be made at initialization time.

# Your heap should support the following public operations:

# .push(): puts a new value into the heap, maintaining the heap property.
# .pop(): removes the "top" value in the heap, maintaining the heap property.
# You will need to implement some private api in order to support those operations.

# The constructor for your heap should default to creating an empty heap, but allow for creating a populated given an iterable as an input.

# For each feature of your heap, start by writing tests to demonstrate that feature.  Then implement the code to pass the tests.

# Update your README with information about your implementation of the Binary Heap data type.  Include all references and collaborations.  

