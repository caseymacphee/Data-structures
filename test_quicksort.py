import pytest
from quicksort import quick_sort

def test_empty():
    newarray = []
    quick_sort(newarray)
    assert len(newarray) == 0

def test_ordered():
    ordered = [0,1,2,3,4,5,6,7,8,9]
    quick_sort(ordered)
    for index, number in enumerate(ordered):
        if index != 0:
            assert number >= ordered[index-1]

def test_decending():
    decending = [9,8,7,6,5,4,3,2,1]
    quick_sort(decending)
    for index, number in enumerate(decending):
        if index != 0:
            assert number >= decending[index-1]

def test_unordered():
    unordered = [3,4,5,3,2,2,445,3,3,5,67,8,9,87,654,0,-50]
    quick_sort(unordered)
    for index, number in enumerate(unordered):
        if index != 0:
            assert number >= unordered[index-1]