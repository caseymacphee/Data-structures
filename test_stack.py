import pytest

from stack import *

def test_stack():
	new_stack = Stack()
	new_stack.push(4)
	new_stack.push(5)
	new_stack.push(6)
	last_val_in = new_stack.pop()
	assert last_val_in == 6

def test_empty():
	with pytest.raises(Exception):
		new_stack = Stack()
		new_stack.push(1)
		new_stack.push(2)
		new_stack.push(3)
		new_stack.pop()
		new_stack.pop()
		new_stack.pop()
		new_stack.pop()

def test_None():
	new_stack = Stack()
	new_stack.push(None)
	last_val_in = new_stack.pop()
	assert last_val_in is None
