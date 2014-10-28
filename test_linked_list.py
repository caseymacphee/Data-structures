import pytest
from linked_list import *

new_list = Linked_list()


def test_insert():
	new_list.insert(1)
	new_list.insert(2)
	new_list.insert(3)
	new_list.insert(4)
	to_string = str(new_list)	
	assert to_string == '(4, 3, 2, 1)'

def test_pop():
	last_in = new_list.pop()
	assert last_in == 4
	last_in = new_list.pop()
	assert last_in == 3
	new_list.pop()
	new_list.pop()
	assert new_list.pop() == None
	assert new_list.pop() == None

def test_size():
	new_list.insert(1)
	new_list.insert(2)
	new_list.insert(6)
	assert new_list.size() == 3
	test_list = Linked_list()
	assert test_list.size() == 0

def test_search():
	found_val = new_list.search(30)
	assert found_val is None
	found_val = new_list.search(2)
	assert found_val.data == 2
	test_list = Linked_list()
	found_val = test_list.search(1)
	assert found_val == None
	test_list.insert(5)
	test_list.insert(None)
	found_val = test_list.search(None)
	assert found_val.data == None

def test_remove():
	new_list.insert(4)
	new_list.insert(5)
	newnode1 = Node(1)
	newnode2 = Node(3)
	newnode3 = Node(5)
	newnode4 = Node(6)
	new_list.remove(newnode1)
	new_list.remove(newnode2)
	new_list.remove(newnode3)
	new_list.remove(newnode4)
	assert str(new_list) == '(4, 2)'
	newnode5 = Node(4)
	newnode6 = Node(2)   
	new_list.remove(newnode5)
	new_list.remove(newnode6)
	assert str(new_list) == '()'
	with pytest.raises(Exception):
		new_list.remove(3)

