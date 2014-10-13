import pytest

from stack import *

def test_stack():
	s = Stack()
	s.push(4)
	s.push(5)
	s.push(6)

	j = s.pop()
	assert j == 6