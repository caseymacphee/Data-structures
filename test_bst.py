from bst import *
import pytest

tree = Binary_search_tree()
tree.insert(5)
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(5)
tree.insert(7)

def test_insert():
	assert tree.root.data == 5
	assert tree.root.left.data == 4
	assert tree.root.left.left.data == 2
	assert tree.root.left.left.right.data == 3
	assert tree.root.right.data == 6
	assert tree.root.right.right.data == 7
	assert tree.root.left.right.data == 5
	
	with pytest.raises(Exception):
		tree.insert(None)
def test_size():
	treesize = tree.size()
	assert treesize == 7
	newtree = Binary_search_tree()
	treesize = newtree.size()
	assert treesize == 0

def test_contains():
	assert tree.contains(1) == False
	assert tree.contains(10) == False
	assert tree.contains(3) == True
	assert tree.contains(5) == True
	assert tree.contains(None) == False
	newtree = Binary_search_tree()
	assert newtree.contains(1) == False
	assert newtree.contains(None) == False

def test_depth():
	assert tree.depth() == 4
	tree.insert(8)
	assert tree.depth() == 4
	tree.insert(9)
	assert tree.depth() == 5
	newtree = Binary_search_tree()
	assert newtree.depth() == 0
	newtree.insert(1)
	assert newtree.depth() == 1

def test_balance():
	newtree = Binary_search_tree()
	assert newtree.balance() == 0
	newtree.insert(5)
	assert newtree.balance() == 0
	newtree.insert(4)
	assert newtree.balance() == 1
	newtree.insert(6)
	assert newtree.balance() == 0
	newtree.insert(7)
	assert newtree.balance() == -1
	newtree.insert(8)
	assert newtree.balance() == -2

def test_traversal():
	newtree = Binary_search_tree()
	newtree.insert(9)
	newtree.insert(11)
	newtree.insert(2)
	newtree.insert(8)
	newtree.insert(6)
	newtree.insert(1)
	newtree.insert(-10)
	newtree.insert(4)

	pre_order_gen = newtree.pre_order()
	assert pre_order_gen.next() == 9
	assert pre_order_gen.next() == 2
	assert pre_order_gen.next() == 1
	assert pre_order_gen.next() == -10
	assert pre_order_gen.next() == 8
	assert pre_order_gen.next() == 6
	assert pre_order_gen.next() == 4
	assert pre_order_gen.next() == 11
	with pytest.raises(Exception):
		pre_order_gen.next()

	in_order_gen = newtree.in_order()
	assert in_order_gen.next() == -10
	assert in_order_gen.next() == 1
	assert in_order_gen.next() == 2
	assert in_order_gen.next() == 4
	assert in_order_gen.next() == 6
	assert in_order_gen.next() == 8
	assert in_order_gen.next() == 9
	assert in_order_gen.next() == 11
	with pytest.raises(Exception):
		in_order_gen.next()

	post_order_gen = newtree.post_order()
	assert post_order_gen.next() == -10
	assert post_order_gen.next() == 1
	assert post_order_gen.next() == 4
	assert post_order_gen.next() == 6
	assert post_order_gen.next() == 8
	assert post_order_gen.next() == 2
	assert post_order_gen.next() == 11
	assert post_order_gen.next() == 9
	with pytest.raises(Exception):
		post_order_gen.next()

	breadth_first_gen = newtree.breadth_first()
	assert breadth_first_gen.next() == 9
	assert breadth_first_gen.next() == 2
	assert breadth_first_gen.next() == 11
	assert breadth_first_gen.next() == 1
	assert breadth_first_gen.next() == 8
	assert breadth_first_gen.next() == -10
	assert breadth_first_gen.next() == 6
	assert breadth_first_gen.next() == 4
	with pytest.raises(Exception):
		breadth_first_gen.next()























