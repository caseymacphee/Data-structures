import pytest
import merge_sort

def test_empty():
    empty_list = []
    returned_list = merge_sort.merge_sort(empty_list)
    assert len(returned_list) == 0

def test_ordered():
    ordered_list = [1,2,3,4,5,6,7,8,9,10]
    returned_list = merge_sort.merge_sort(ordered_list)
    for index, number in enumerate(returned_list):
        if index != 0:
            assert number >= returned_list[index-1]

def test_decending():
    decending_list = [10,9,8,7,6,5,4,3,2,1]
    returned_list = merge_sort.merge_sort(decending_list)
    for index, number in enumerate(returned_list):
        if index != 0:
            assert number >= returned_list[index-1]

def test_unordered():
    decending_list = [2,2,67,5,2,2,4,5,63,12,90908,2,1,34,0]
    returned_list = merge_sort.merge_sort(decending_list)
    for index, number in enumerate(returned_list):
        if index != 0:
            assert number >= returned_list[index-1]