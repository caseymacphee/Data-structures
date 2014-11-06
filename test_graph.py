##test_graph.py##

import pytest
from graph import *

def test_nodes():
	new_graph = Graph()
	assert len(new_graph.nodes) == 0

def test_add():
	new_graph = Graph()
	new_graph.add_node(None)
	assert len(new_graph.nodes) == 1
	new_graph.add_node('Clouds')
	new_graph.add_node(9)
	new_graph.add_node([1,2,3])
	assert len(new_graph.nodes) == 4
	assert new_graph.nodes[1].data == 'Clouds'
	assert new_graph.nodes[2].data == 9
	assert new_graph.nodes[3].data == [1,2,3]

def test_edge():
	new_graph = Graph()
	new_graph.add_edge('Earth', 'Wind')
	new_graph.add_edge('Wind', 'Fire')
	assert len(new_graph.edges) == 2
	assert str(new_graph.edges[0]) == '(Earth, Wind)'
	assert str(new_graph.edges[1]) == '(Wind, Fire)'
	assert new_graph.nodes[0].data == 'Earth'
	assert new_graph.nodes[1].data == 'Wind'
	assert new_graph.nodes[2].data == 'Fire'
	with pytest.raises(Exception):
		assert new_graph.nodes[3] == "It shouldn't add wind twice"

def test_del():
	new_graph = Graph()
	new_graph.add_edge('Earth', 'Wind')
	new_graph.add_edge('Wind', 'Fire')
	new_graph.del_node('Earth')
	assert new_graph.nodes[0].data == 'Wind'
	assert str(new_graph.edges[0]) == '(Wind, Fire)'
	with pytest.raises(Exception):
		new_graph.del_node('Water')

def test_del_edge():
	new_graph = Graph()
	new_graph.add_edge('Earth', 'Wind')
	new_graph.add_edge('Wind', 'Fire')
	new_graph.del_edge('Earth', 'Wind')
	assert len(new_graph.edges) == 1
	assert str(new_graph.edges[0]) == '(Wind, Fire)'
	with pytest.raises(Exception):
		new_graph.del_edge('Earth', 'Water')

def test_has():
	new_graph = Graph()
	new_graph.add_edge('Earth', 'Wind')
	new_graph.add_edge('Wind', 'Fire')
	assert new_graph.has_node('Water') == False
	assert new_graph.has_node('Wind') == True

	new_graph = Graph()
	assert new_graph.has_node(None) == False

def test_neighbors():
	new_graph = Graph()
	new_graph.add_edge('Earth', 'Wind')
	new_graph.add_edge('Wind', 'Fire')
	new_graph.add_edge('Water', 'Earth')
	wind_neighbors = new_graph.neighbors('Wind')
	assert 'Earth' in wind_neighbors and 'Fire' in wind_neighbors
	assert 'Water' not in wind_neighbors

def test_adjacent():
	new_graph = Graph()
	new_graph.add_edge('Earth', 'Wind')
	new_graph.add_edge('Wind', 'Fire')
	new_graph.add_edge('Water', 'Earth')
	assert new_graph.adjacent('Earth', 'Wind')
	assert new_graph.adjacent('Wind', 'Earth')
	assert new_graph.adjacent('Stones', 'Wind') == False
	assert new_graph.adjacent('Water', 'Wind') == False






