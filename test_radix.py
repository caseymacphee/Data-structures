import pytest
import radix_sort

def test_empty():
    empty = []
    returned = radix_sort.radix_sort(empty)
    assert len(returned) == 0

def test_ordered():
    ordered = [1,2,3,4,5,6,7,8,9]
    returned = radix_sort.radix_sort(ordered)
    for index, number in enumerate(returned):
        if index != 0:
            assert number >= returned[index-1]

def test_decending():
    decending = [9,8,7,6,5,4,3,2,1]
    returned = radix_sort.radix_sort(decending)
    for index, number in enumerate(returned):
        if index != 0:
            assert number >= returned[index-1]
def test_unordered():
    unordered = [4,23,2,4,4,56,87,65,432,1,0,7,5,4,3,3,33]
    returned = radix_sort.radix_sort(unordered)
    for index, number in enumerate(returned):
        if index != 0:
            assert number >= returned[index-1]
