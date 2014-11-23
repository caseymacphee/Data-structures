def insertion_sort(unsorted_list):
    """
    This sort function works by progressivley selecting the next item in the unsorted_list
    starting from the begining and checking all previous all sorted numbers
    until it finds it's sorted order. 
    The best case for this algorithm is O(n) if the elements are already sorted
    The worst case is O(n^2) if the elements are in decending order of value.
    """
    for element in xrange(len(unsorted_list)):
        current = element
        while current > 0 and unsorted_list[current - 1] > unsorted_list[current]:
            ### Switch the values ###
            unsorted_list[current - 1], unsorted_list[current] = unsorted_list[current], unsorted_list[current -1]
            current -= 1
    sorted_list = unsorted_list
    return sorted_list
if __name__ == '__main__':

    newlist = [1,2,3,6,3,2,5,7,5,8,0,7,5,3,2,2,11]
    print newlist
    sortedlist = insertion_sort(newlist)
    print sortedlist

    newlist2 = [9,8,7,6,5,4,3,2,1]
    print newlist2
    sortedlist2 = insertion_sort(newlist2)
    print sortedlist2
    print insertion_sort.func_doc