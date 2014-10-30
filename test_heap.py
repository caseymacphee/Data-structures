import pytest
from heap import *

def test_push():
	newheap = Min_heap()
	newheap.push(8)
	newheap.push(6)
	newheap.push(2)
	newheap.push(9)
	newheap.push(13)
	newheap.push(7)
	newheap.push(20)
	newheap.push(1)
	assert newheap.size() == 8
	assert newheap._pile == [None, 1, 2, 6, 8, 13, 7, 20, 9]
	with pytest.raises(Exception):
		newheap.push(None)
	with pytest.raises(Exception):
		noncomparableobj = 'A string'
		newheap.push(noncomparableobj)

def test_pop():
	newheap = Min_heap()
	newheap.push(8)
	newheap.push(6)
	newheap.push(2)
	newheap.push(9)
	newheap.push(13)
	newheap.push(7)
	newheap.push(20)
	newheap.push(1)

	ordered_list = []
	while newheap.size() > 0:
		ordered_list.append(newheap.pop())
	assert ordered_list == [1,2,6,7,8,9,13,20]
	nothing_left = None
	assert nothing_left == newheap.pop()
	assert newheap.size() == 0

def test_populate():
	input_list = [8,6,2,9,13,7,20,1]
	newheap = Min_heap(input_list)
	ordered_list = []
	while newheap.size() > 0:
		ordered_list.append(newheap.pop())
	assert ordered_list == [1,2,6,7,8,9,13,20]
	




