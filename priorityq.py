class Priority_node:
	def __init__(self, data, priority):
		self.data = data
		self.priority = priority
	def __str__(self):
		return '({}, {})'.format(self.data,self.priority)

class Priority_queue(object):

	def __init__(self):
		self._pile = []
		self._pile.insert(0, None)
		self.current_size = 0
	
	def insert(self, item):
		if 'data' not in dir(item) or 'priority' not in dir(item):
			raise Exception("Item must be of type Priority_node")
		if item.priority < 1 or item.priority > 10:
			raise Exception("Item must have a priority of 1-10")
		self.current_size += 1
		self._pile.append(item)
		index = len(self._pile) - 1
		while self._pile[index/2] is not None and item.priority < self._pile[index/2].priority:
			swap = self._pile[index/2]
			self._pile[index] = swap
			self._pile[index/2] = item
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
				if (index * 2) + 1 < len(self._pile): 
					if self._pile[index].priority > self._pile[index*2].priority:
						##greater than * 2, is * 2 + 1 less than both?
						if self._pile[index].priority > self._pile[index*2 + 1].priority:
							## also greater than *2 + 1
							if self._pile[index * 2].priority > self._pile[index * 2 + 1].priority:
								## * 2 + 1 is lesser, switch with that
								self._pile[index] = self._pile[index*2 + 1]
								self._pile[index*2 + 1] = current
								index = index * 2 + 1
							else:
								## *2 is lesser switch with that
								self._pile[index] = self._pile[index * 2]
								self._pile[index * 2] = current
								index = index * 2
						else:
							self._pile[index] = self._pile[index*2]
							self._pile[index*2] = current
							index = index * 2
					elif self._pile[index].priority > self._pile[index * 2 + 1].priority:
						# not greater than * 2
						self._pile[index] = self._pile[index*2 + 1]
						self._pile[index*2 + 1] = current
						index = (index * 2) + 1
					else:
						break
				else:
					## can only test *2	
					if self._pile[index].priority > self._pile[index * 2].priority:
						self._pile[index] = self._pile[index*2]
						self._pile[index*2] = current
						index = index * 2
					else:
						break
			return min
	def peek(self):
		if self.size() < 1:
			return None
		top_priority = self._pile[1]
		return top_priority
	def size(self):
		return self.current_size
