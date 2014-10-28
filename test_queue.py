import pytest

from queue import *

def test_enqueue():
	new_q = Queue()
	new_q.enqueue(1)
	new_q.enqueue(2)
	new_q.enqueue(3)
	new_q.enqueue(4)
	new_q.enqueue(5)
	assert new_q.head.data == 5

def test_dequeue():
	new_q = Queue()
	new_q.enqueue(1)
	new_q.enqueue(2)
	new_q.enqueue(3)
	new_q.enqueue(4)
	new_q.enqueue(5)
	val = new_q.dequeue()
	assert val == 1
	val = new_q.dequeue()
	assert val == 2
	val = new_q.dequeue()
	assert val == 3
	val = new_q.dequeue()
	assert val == 4
	val = new_q.dequeue()
	assert val == 5
	with pytest.raises(Exception):
		fail_q = Queue()
		fail_q.dequeue()

def test_size():
	new_q = Queue()
	new_q.enqueue(1)
	new_q.enqueue(2)
	new_q.enqueue(3)
	new_q.enqueue(4)
	new_q.enqueue(5)
	assert new_q.size() == 5
	new_q.dequeue()
	new_q.dequeue()
	assert new_q.size() == 3
	new_q.dequeue()
	new_q.dequeue()
	new_q.dequeue()
	assert new_q.size() == 0
