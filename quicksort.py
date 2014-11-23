from insertion_sort import insertion_sort

def quick_sort(unsorted_list, first = 0, last = None):
    """
    This function quick_sort at it's worst sorts in O(n^2)
    and on average is O(n log n)
    The algorithm works by deviding based on a pivot and swapping values
    that are greater or less than the pivot and on the wrong side.
    This is done on smaller and smaller sub arrays until the array is sorted.
    """
    if last is None:
        last = len(unsorted_list)
    size = last - first
    if size < 2:
        return

    mid = size // 2 + first
    pivots = [unsorted_list[first], unsorted_list[mid], unsorted_list[last - 1]]
    insertion_sort(pivots)
    pivot = pivots[1]
    left = first
    right = last - 1

    while left <= right:
        while unsorted_list[left] < pivot:
            left += 1
        while unsorted_list[right] > pivot:
            right -= 1
        if left <= right:
            unsorted_list[left], unsorted_list[right] = unsorted_list[right], unsorted_list[left]
            left += 1
            right -= 1
    quick_sort(unsorted_list, first, right + 1)
    quick_sort(unsorted_list, left, last)

if __name__ == '__main__':
    newlist = [1,2,3,4,5,6,7,8]
    print newlist
    quick_sort(newlist)
    print newlist
    newlist2 = [9,8,7,6,5,4,3,2,1]
    print newlist2
    quick_sort(newlist2)
    print newlist2
    newlist3 = [5,3,3,6,78,88,5,32,1,1,2,332,1]
    print newlist3
    quick_sort(newlist3)
    print newlist3
    print quick_sort.func_doc
