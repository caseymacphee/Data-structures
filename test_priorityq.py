import pytest
from priorityq import *

n1 = Priority_node(10,3)
n2 = Priority_node(5,3)
n3 = Priority_node(5,5)
n4 = Priority_node(7,1)
n5 = Priority_node(10,1)
n6 = Priority_node(30,2)
n7 = Priority_node(1,5)
n8 = Priority_node(23,10)
n9 = Priority_node('Test', 2)
n10 = Priority_node(True, 3)
n11 = Priority_node(None, 5)

def test_insert():
	newq = Priority_queue()
	newq.insert(n1)
	newq.insert(n2)
	newq.insert(n3)
	newq.insert(n4)
	newq.insert(n5)
	newq.insert(n6)
	newq.insert(n7)
	newq.insert(n8)
	newq.insert(n9)
	newq.insert(n10)
	newq.insert(n11)
	assert newq._pile[1].data == 7
	assert newq._pile[2].data == 10
	assert newq._pile[3].data == 30
	assert newq._pile[4].data == 'Test'
	assert newq._pile[5].data == 10
	assert newq._pile[6].data == 5
	assert newq._pile[7].data == 1
	assert newq._pile[8].data == 23
	assert newq._pile[9].data == 5
	assert newq._pile[10].data == True
	assert newq._pile[11].data == None
	assert newq.size() == 11
def test_pop():

	newq = Priority_queue()
	newq.insert(n1)
	newq.insert(n2)
	newq.insert(n3)
	newq.insert(n4)
	newq.insert(n5)
	newq.insert(n6)
	newq.insert(n7)
	newq.insert(n8)
	newq.insert(n9)
	newq.insert(n10)
	priority_list = []
	while newq.size() > 0:
		priority_list.append(newq.pop())
	assert priority_list[0].priority == 1
	assert priority_list[1].priority == 1
	assert priority_list[2].priority == 2
	assert priority_list[3].priority == 2
	assert priority_list[4].priority == 3
	assert priority_list[5].priority == 3
	assert priority_list[6].priority == 3
	assert priority_list[7].priority == 5
	assert priority_list[8].priority == 5
	assert priority_list[9].priority == 10
	assert newq.pop() == None
	assert newq.size() == 0

def test_peek():
	newq = Priority_queue()
	newq.insert(n1)
	newq.insert(n2)
	newq.insert(n3)
	newq.insert(n4)
	newq.insert(n5)
	assert newq.peek().data == 7
	assert newq.peek().priority == 1
	newq.pop()
	assert newq.peek().data == 10
	assert newq.peek().priority == 1
	newq.pop()
	assert newq.peek().data == 5
	assert newq.peek().priority == 3
	newq.pop()
	assert newq.peek().data == 10
	assert newq.peek().priority == 3
	newq.pop()
	assert newq.peek().data == 5
	assert newq.peek().priority == 5
	newq.pop()
	assert newq.peek() == None
