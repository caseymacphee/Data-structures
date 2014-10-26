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

def test_depth():
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
