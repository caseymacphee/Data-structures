from math import log

def getNum(num, base, digit_num):
    return (num // base ** digit_num) % base

def makeBlanks(size):
    return [[] for _ in xrange(size)]

def split(currentlist, base, dig_num):
    buckets = makeBlanks(base)
    for number in currentlist:
        buckets[getNum(number, base, dig_num)].append(number)
    return buckets

def merge(currentlist):
    newlist = []
    for sub in currentlist:
        newlist.extend(sub)
    return newlist

def maxAbs(currentlist):
    return max(abs(num) for num in currentlist)

def radix_sort(currentlist, base = 10):
    """
    Radix_sort uses digits that share the same significant position for the comparison,
    and the the worst case runtime is O(kN), where k is the length of significant figures.
    """
    if len(currentlist) < 2:
        return currentlist
    passes = int(round(log(maxAbs(currentlist), base)) + 1)
    newlist = currentlist[:]
    for dig_num in xrange(passes):
        newlist = merge(split(newlist, base, dig_num))
    return newlist

if __name__ == '__main__':
    ordered = [1,2,3,4,5,6,7,8,9]
    print ordered
    returned = radix_sort(ordered)
    print returned
    decending = [9,8,7,6,5,4,3,2,1]
    print decending
    returned = radix_sort(decending)
    print returned
    unordered = [3,4,5,3,2,1,4,6,8,9,65,3,2,0]
    print unordered
    returned = radix_sort(unordered)
    print returned
    print radix_sort.func_doc

