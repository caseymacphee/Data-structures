class Tree_node(object):
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)

class Binary_search_tree(object):
	def __init__(self):
		self.root = None
		self.currentSize = 0

	def insert(self, val):
		if val is None:
			raise Exception('None type is not sortable')
		newNode = Tree_node()
		newNode.data = val 
		self.currentSize += 1
		if self.root == None:
			self.root = newNode
		else:
			current = self.root
			while True:
				if current.data > val:
					if current.left is None:
						current.left = newNode 
						break
					else:
						current = current.left
				elif current.data < val:
					if current.right is None:
						current.right = newNode
						break
					else:
						current = current.right
				else:
					if current.left is None:
						current.right = newNode
						break
					else:
						current = current.left
	def contains(self, val):
		if self.root is None:
			return False
		current = self.root
		while current is not None:
			if current.data > val:
				current = current.left
			elif current.data < val:
				current = current.right
			else:
				return True
		return False

	def size(self):
		return self.currentSize
	
	def depth(self):
		current = self.root
		maxDepth = self.__max_depth(current)
		return maxDepth
	
	def __max_depth(self, node):
		if node is None:
			return 0
		else:
			leftD = self.__max_depth(node.left)
			rightD = self.__max_depth(node.right)
			if leftD > rightD:
				return leftD + 1
			else:
				return rightD + 1

	def balance(self):
		if self.root is None:
			return 0
		leftSide = self.root.left
		rightSide = self.root.right
		leftHeight = self.__max_depth(leftSide)
		rightHeight = self.__max_depth(rightSide)
		return leftHeight - rightHeight









