import pytest

from stack import *

def test_stack():
	s = Stack()
	s.push(4)
	s.push(5)
	s.push(6)
	j = s.pop()
	assert j == 6

def test_empty():
	with pytest.raises(Exception):
		s = Stack()
		s.push(1)
		s.push(2)
		s.push(3)
		s.pop()
		s.pop()
		s.pop()
		s.pop()

def test_None():
	s = Stack()
	s.push(None)
	none = s.pop()
	assert none is None
