import pytest

from queue import *

def test_enqueue():
	newq = Queue()
	newq.enqueue(1)
	newq.enqueue(2)
	newq.enqueue(3)
	newq.enqueue(4)
	newq.enqueue(5)
	assert newq.head.data == 5

def test_dequeue():
	newq = Queue()
	newq.enqueue(1)
	newq.enqueue(2)
	newq.enqueue(3)
	newq.enqueue(4)
	newq.enqueue(5)
	val = newq.dequeue()
	assert val == 1
	val = newq.dequeue()
	assert val == 2
	val = newq.dequeue()
	assert val == 3
	val = newq.dequeue()
	assert val == 4
	val = newq.dequeue()
	assert val == 5

def test_size():
	newq = Queue()
	newq.enqueue(1)
	newq.enqueue(2)
	newq.enqueue(3)
	newq.enqueue(4)
	newq.enqueue(5)
	assert newq.size == 5
	newq.dequeue()
	newq.dequeue()
	assert newq.size == 3
	newq.dequeue()
	newq.dequeue()
	newq.dequeue()
	assert newq.size == 0
