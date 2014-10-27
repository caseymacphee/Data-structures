import pytest
from d_linked_list import *

newlist = D_linked_list()


def test_insert():
	newlist.insert(1)
	newlist.insert(2)
	newlist.insert(3)
	newlist.insert(4)
	tostring = str(newlist)	
	assert tostring == '(4, 3, 2, 1)'

def test_pop():
	lastin = newlist.pop()
	assert lastin == 4
	lastin = newlist.pop()
	assert lastin == 3
	newlist.pop()
	newlist.pop()
	assert newlist.pop() == None
	assert newlist.pop() == None

def test_size():
	newlist.insert(1)
	newlist.insert(2)
	newlist.insert(6)
	assert newlist.size() == 3
	testlist = D_linked_list()
	assert testlist.size() == 0

def test_remove():
	newlist.insert(4)
	newlist.insert(5)
	newnode1 = Node(1)
	newnode2 = Node(3)
	newnode3 = Node(5)
	newnode4 = Node(6)
	newlist.remove(newnode2)
	newlist.remove(newnode3)
	newlist.remove(newnode4)
	assert str(newlist) == '(4, 2, 1)'
	newnode5 = Node(4)
	newnode6 = Node(2)   
	newlist.remove(newnode5)
	newlist.remove(newnode6)
	newlist.remove(newnode1)
	assert str(newlist) == '()'
	with pytest.raises(Exception):
		newlist.remove(3)

def test_shift():
	dlist = D_linked_list()
	dlist.insert(1)
	dlist.insert(2)
	dlist.insert(3)
	dlist.insert(4)
	dlist.insert(5)
	last = dlist.shift()
	assert last == 1
	dlist.shift()
	dlist.shift()
	dlist.shift()
	dlist.shift()
	dlist.shift()
	assert dlist.shift() == None
