import pytest
from d_linked_list import *

s = D_linked_list()


def test_insert():
	
	s.insert(1)
	s.insert(2)
	s.insert(3)
	s.insert(4)
	y = str(s)
	assert y == '(4, 3, 2, 1)'

def test_pop():
	x = s.pop()
	assert x == 4

def test_size():
	assert s.size == 3

def test_search():
	j = s.search(30)
	assert j is None

	i = s.search(2)
	assert i.data == 2

def test_remove():
	s.insert(4)
	s.insert(5)
	s.remove(1)
	s.remove(3)
	s.remove(5)
	assert str(s) == '(4, 2)'

def test_shift():
	s = D_linked_list()
	s.insert(5)
	s.insert(4)
	s.insert(3)
	s.insert(2)
	s.insert(1)
	end = s.shift()
	assert end == 5
	assert s.size == 4
	s.shift()
	s.shift()
	s.shift()
	s.shift()
	end = s.shift()
	assert end is None
	assert s.size == 0
