from queue import *

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

	def balance(self, start):
		if start is None:
			return 0
		leftSide = start.left
		rightSide = start.right
		leftHeight = self.__max_depth(leftSide)
		rightHeight = self.__max_depth(rightSide)
		return leftHeight - rightHeight

	def pre_order(self):
		top = self.root
		pre_order_list = []
		self._pre_order(top, pre_order_list)
		return (item for item in pre_order_list)

	def _pre_order(self, current, gen_list):
		gen_list.append(current.data)
		if current.left is not None:
			self._pre_order(current.left, gen_list)
		if current.right is not None:
			self._pre_order(current.right, gen_list)

	def post_order(self):
		top = self.root
		post_order_list = []
		self._post_order(top, post_order_list)
		return (item for item in post_order_list)

	def _post_order(self, current, gen_list):
		if current.left is not None:
			self._post_order(current.left, gen_list)
		if current.right is not None:
			self._post_order(current.right, gen_list)
		gen_list.append(current.data)

	def in_order(self):
		top = self.root
		in_order_list = []
		self._in_order(top, in_order_list)
		return (item for item in in_order_list)

	def _in_order(self, current, gen_list):
		if current.left is not None:
			self._in_order(current.left, gen_list)
		gen_list.append(current.data)
		if current.right is not None:
			self._in_order(current.right, gen_list)
	
	def breadth_first(self):
		breadth_first_list = []
		breadth_q = Queue()
		breadth_q.enqueue(self.root)
		while breadth_q.size > 0:
			last_out = breadth_q.dequeue()
			breadth_first_list.append(last_out.data)
			if last_out.left is not None:
				breadth_q.enqueue(last_out.left)
			if last_out.right is not None:
				breadth_q.enqueue(last_out.right)
		return (item for item in breadth_first_list)

	def adjust_balance(self):
		current_balance = self.balance(self.root)
		while current_balance > 1 or current_balance < -1:
			if current_balance < -1:
				temp = self.root
				self.root = self.root.right
				temp.right = None
				self._recombine(temp)
			elif current_balance > 1:
				temp = self.root
				self.root = self.root.left
				temp.left = None
				self._recombine(temp)
			current_balance = self.balance(self.root)

	def _recombine(self, node):
		val = node.data
		current = self.root
		while True:
			if current.data > val:
				if current.left is None:
					current.left = node 
					break
				else:
					current = current.left
			elif current.data < val:
				if current.right is None:
					current.right = node
					break
				else:
					current = current.right
			else:
				if current.left is None:
					current.right = node
					break
				else:
						current = current.left	

	def avl_balance(self):
		current_balance = self.balance(self.root)
		while current_balance > 1 or current_balance < -1:
			### Left subtree is larger than right ###
			if current_balance > 1:
				### Left/Right case ###
				if self.balance(self.root.left) < 0:
					self.rotate_left(self.root.left)

				### Left/Left case ###
				self.rotate_right(self.root)
			### Right subree is larger than left ###
			if current_balance < -1:

				### Right/Left case ###
				if self.balance(self.root.right) > 0:
					self.rotate_right()
				### Right/Right case ###
				self.rotate_left(self.root)
			current_balance = self.balance(self.root)

	def rotate_right(self, start):
		new_root = self.root.left
		new_left_sub = new_root.right
		prev_root = self.root
		self.root = new_root
		prev_root.left = new_left_sub
		new_root.right = prev_root

	def rotate_left(self, start):
		new_root = self.root.right
		new_left_sub = new_root.left
		prev_root = self.root
		self.root = new_root
		prev_root.right = new_left_sub
		new_root.left = prev_root


















