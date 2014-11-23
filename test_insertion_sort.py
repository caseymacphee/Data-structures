import pytest
import insertion_sort

def test_ordered():
    ordered_list = [1,2,3,4,5,6,7]
    after_sort = insertion_sort.insertion_sort(ordered_list)
    for index, number in enumerate(after_sort):
        if index != 0:
            assert number >= after_sort[index-1]

def test_unordered():
    unordered_list = [3,4,2,2,5,7,8,2,2,3,10,0]
    after_sort = insertion_sort.insertion_sort(unordered_list)
    for index, number in enumerate(after_sort):
        if index != 0:
            assert number >= after_sort[index-1]

def test_reverse_order():
    decending_list = [9,8,7,6,5,4,3,2,1]
    after_sort = insertion_sort.insertion_sort(decending_list)
    for index, number in enumerate(after_sort):
        if index != 0:
            assert number >= after_sort[index-1]