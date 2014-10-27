import pytest
from linked_list import *

newlist = Linked_list()


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
	testlist = Linked_list()
	assert testlist.size() == 0

def test_search():
	foundval = newlist.search(30)
	assert foundval is None
	foundval = newlist.search(2)
	assert foundval.data == 2
	testlist = Linked_list()
	foundval = testlist.search(1)
	assert foundval == None
	testlist.insert(5)
	testlist.insert(None)
	foundval = testlist.search(None)
	assert foundval.data == None

def test_remove():
	newlist.insert(4)
	newlist.insert(5)
	newnode1 = Node(1)
	newnode2 = Node(3)
	newnode3 = Node(5)
	newnode4 = Node(6)
	newlist.remove(newnode1)
	newlist.remove(newnode2)
	newlist.remove(newnode3)
	newlist.remove(newnode4)
	assert str(newlist) == '(4, 2)'
	newnode5 = Node(4)
	newnode6 = Node(2)   
	newlist.remove(newnode5)
	newlist.remove(newnode6)
	assert str(newlist) == '()'

