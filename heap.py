class Min_heap(object):

	def __init__(self, iterable = None):
		self.pile = []
		self.pile.insert(0, None)
		if iterable is not None:
			try:
				populate_iterable = iter(iterable)
				try:
					iterate = True
					while iterate:
						self.push(populate_iterable.next())
				except StopIteration:
					print "Min heap populated"
			except:
				raise Exception("Object must be iterable to populate min heap")	

	def push(self, val):
		if val is None:
			raise Exception('None type is not sortable')
		self.pile.append(val)
		index = len(self.pile) - 1
		while val < self.pile[index/2] and self.pile[index/2] is not None:
			swap = self.pile[index/2]
			self.pile[index] = swap
			self.pile[index/2] = val
			index = index/2

	def pop(self):
		if len(self.pile) == 1:
			return None
		elif len(self.pile) == 2:
			return self.pile.pop()
		else:
			min = self.pile[1]
			lastelement = self.pile.pop()
			self.pile[1] = lastelement
			index = 1
			while (index * 2) < len(self.pile):
				current = self.pile[index]
				if len(self.pile) > (index * 2) + 1: 
					if self.pile[index] > self.pile[index * 2]:
						if self.pile[index*2] < self.pile[index*2 + 1]:
							self.pile[index] = self.pile[index*2]
							self.pile[index*2] = current
							index = index * 2
						else:
							self.pile[index] = self.pile[index*2 + 1]
							self.pile[index*2 + 1] = current
							index = (index * 2) + 1
				elif self.pile[index] > self.pile[index * 2]:
						self.pile[index] = self.pile[index*2]
						self.pile[index*2] = current
						index = index * 2
			return min

# For an additional challenge, implement f.pile that can be either and allow the choice to be made at initialization time.

# Youf.pile should support the following public operations:

# .push(): puts a new value into thf.pile, maintaining thf.pile property.
# .pop(): removes the "top" value in thf.pile, maintaining thf.pile property.
# You will need to implement some private api in order to support those operations.

# The constructor for youf.pile should default to creating an emptf.pile, but allow for creating a populated given an iterable as an input.

# For each feature of youf.pile, start by writing tests to demonstrate that feature.  Then implement the code to pass the tests.

# Update your README with information about your implementation of the Binary Heap data type.  Include all references and collaborations.  

