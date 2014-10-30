class Min_heap(object):

	def __init__(self, iterable = None):
		self._pile = []
		self._pile.insert(0, None)
		self.current_size = 0
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
		if '__cmp__' not in dir(val):
			raise Exception('Object must be comparable')
		self.current_size += 1
		self._pile.append(val)
		index = len(self._pile) - 1
		while val < self._pile[index/2] and self._pile[index/2] is not None:
			swap = self._pile[index/2]
			self._pile[index] = swap
			self._pile[index/2] = val
			index = index/2

	def pop(self):
		if len(self._pile) == 1:
			return None
		elif len(self._pile) == 2:
			self.current_size -= 1
			return self._pile.pop()
		else:
			self.current_size -= 1
			min = self._pile[1]
			lastelement = self._pile.pop()
			self._pile[1] = lastelement
			index = 1
			while (index * 2) < len(self._pile):
				current = self._pile[index]
				if len(self._pile) > (index * 2) + 1: 
					if self._pile[index] > self._pile[index * 2]:
						if self._pile[index*2] < self._pile[index*2 + 1]:
							self._pile[index] = self._pile[index*2]
							self._pile[index*2] = current
							index = index * 2
						else:
							self._pile[index] = self._pile[index*2 + 1]
							self._pile[index*2 + 1] = current
							index = (index * 2) + 1
				elif self._pile[index] > self._pile[index * 2]:
						self._pile[index] = self._pile[index*2]
						self._pile[index*2] = current
						index = index * 2
			return min
	def size(self):
		return self.current_size
